import numpy as np
from playhouse.postgres_ext import *

import jesse.helpers as jh
import jesse.services.logger as logger
import jesse.services.selectors as selectors
from jesse.config import config
from jesse.services.db import db
from jesse.services.notifier import notify
from jesse.enums import order_types, order_statuses, order_roles, order_flags

class Order(Model):
    # id generated by Jesse for database usage
    id = UUIDField(primary_key=True)
    trade_id = UUIDField(index=True)

    # id generated by market, used in live-trade mode
    exchange_id = CharField()
    # some exchanges might require even further info
    vars = JSONField(default={})

    symbol = CharField()
    exchange = CharField()
    side = CharField()
    type = CharField()
    flag = CharField(null=True)
    qty = FloatField()
    price = FloatField(default=np.nan)
    status = CharField(default=order_statuses.ACTIVE)
    created_at = BigIntegerField()
    executed_at = BigIntegerField(null=True)
    canceled_at = BigIntegerField(null=True)
    role = CharField(null=True)
    submitted_via = None

    class Meta:
        database = db
        indexes = ((('exchange', 'symbol'), False),)

    def __init__(self, attributes: dict = None, **kwargs) -> None:
        Model.__init__(self, attributes=attributes, **kwargs)

        if attributes is None:
            attributes = {}

        for a in attributes:
            setattr(self, a, attributes[a])

        if self.created_at is None:
            self.created_at = jh.now_to_timestamp()

        if jh.is_live() and config['env']['notifications']['events']['submitted_orders']:
            self.notify_submission()
        if jh.is_debuggable('order_submission'):
            logger.info(
                f'{"QUEUED" if self.is_queued else "SUBMITTED"} order: {self.symbol}, {self.type}, {self.side}, {self.qty}, ${round(self.price, 2)}'
            )

        # handle exchange balance for ordered asset
        e = selectors.get_exchange(self.exchange)
        e.on_order_submission(self)

    def notify_submission(self) -> None:
        notify(
            f'{"QUEUED" if self.is_queued else "SUBMITTED"} order: {self.symbol}, {self.type}, {self.side}, {self.qty}, ${round(self.price, 2)}'
        )

    @property
    def is_canceled(self) -> bool:
        return self.status == order_statuses.CANCELED

    @property
    def is_active(self) -> bool:
        return self.status == order_statuses.ACTIVE

    @property
    def is_queued(self) -> bool:
        """
        Used in live mode only: it means the strategy has considered the order as submitted,
        but the exchange does not accept it because of the distance between the current
        price and price of the order. Hence it's been queued for later submission.

        :return: bool
        """
        return self.status == order_statuses.QUEUED

    @property
    def is_new(self) -> bool:
        return self.is_active

    @property
    def is_executed(self) -> bool:
        return self.status == order_statuses.EXECUTED

    @property
    def is_filled(self) -> bool:
        return self.is_executed

    @property
    def is_reduce_only(self) -> bool:
        return self.flag == order_flags.REDUCE_ONLY

    @property
    def is_close(self) -> bool:
        return self.flag == order_flags.CLOSE

    @property
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'exchange_id': self.exchange_id,
            # 'session_id': self.session_id,
            'symbol': self.symbol,
            'side': self.side,
            'type': self.type,
            'qty': self.qty,
            'price': self.price,
            'flag': self.flag,
            'status': self.status,
            'created_at': self.created_at,
            'canceled_at': self.canceled_at,
            'executed_at': self.executed_at,
        }

    def cancel(self, silent=False) -> None:
        if self.is_canceled or self.is_executed:
            return

        self.canceled_at = jh.now_to_timestamp()
        self.status = order_statuses.CANCELED

        if not silent:
            if jh.is_debuggable('order_cancellation'):
                logger.info(
                    f'CANCELED order: {self.symbol}, {self.type}, {self.side}, {self.qty}, ${round(self.price, 2)}'
                )
            if jh.is_live() and config['env']['notifications']['events']['cancelled_orders']:
                notify(
                    f'CANCELED order: {self.symbol}, {self.type}, {self.side}, {self.qty}, {round(self.price, 2)}'
                )

        # handle exchange balance
        e = selectors.get_exchange(self.exchange)
        e.on_order_cancellation(self)

    def execute(self, silent=False) -> None:
        if self.is_canceled or self.is_executed:
            return

        self.executed_at = jh.now_to_timestamp()
        self.status = order_statuses.EXECUTED

        if not silent:
            # log
            if jh.is_debuggable('order_execution'):
                logger.info(
                    f'EXECUTED order: {self.symbol}, {self.type}, {self.side}, {self.qty}, ${round(self.price, 2)}'
                )
            # notify
            if jh.is_live() and config['env']['notifications']['events']['executed_orders']:
                notify(
                    f'EXECUTED order: {self.symbol}, {self.type}, {self.side}, {self.qty}, {round(self.price, 2)}'
                )

        p = selectors.get_position(self.exchange, self.symbol)

        if p:
            p._on_executed_order(self)

        # handle exchange balance for ordered asset
        e = selectors.get_exchange(self.exchange)
        e.on_order_execution(self)

    def execute_partially(self, order, order_dict: dict):
        """
        This is a half-dirty workaround for partially executed orders. I moved it here so I can write
        a unit test for it, otherwise there's no point in using it in modes other than live.
        """
        from jesse.store import store

        order.price = jh.float_or_none(order_dict['price'])

        # cancel previous order
        order.cancel(silent=True)

        po = selectors.get_position(order.exchange, order_dict['symbol'])

        # create two orders
        filled_order = Order({
            'id': jh.generate_unique_id(),
            'symbol': order_dict['symbol'],
            'exchange': order.exchange,
            'side': order_dict['side'],
            'type': order_types.MARKET,
            'flag': order.flag,
            'qty': jh.prepare_qty(order_dict['filled_qty'], order_dict['side']),
            'price': order_dict['price'],
            'role': order.role,
            'submitted_via': order.submitted_via
        })
        filled_order.execute(silent=True)

        remaining_qty = jh.prepare_qty(
            abs(order.qty) - abs(order_dict['filled_qty']), order_dict['side']
        )
        remaining_order = Order({
            'id': jh.generate_unique_id(),
            'symbol': order_dict['symbol'],
            'exchange': order.exchange,
            'side': order_dict['side'],
            'type': order.type,
            'flag': order.flag,
            'qty': remaining_qty,
            'price': order_dict['price'],
            'role': order.role,
            'submitted_via': order.submitted_via
        })
        store.orders.add_order(remaining_order)

        logger.info(
            f"PARTIALLY FILLED: {order.symbol}, {order.side}, {order_dict['filled_qty']}/{order.qty}, {order.price}. "
            f'Remaining qty was submitted as a new LIMIT order with qty of {remaining_order.qty}'
        )

        # to make sure it is possible to update entry/exit orders in the strategy, add it to its list:
        po.strategy._close_position_orders.append(remaining_order)


if not jh.is_unit_testing():
    # create the table
    Order.create_table()
