from playhouse.postgres_ext import *

import jesse.helpers as jh
import jesse.services.logger as logger
import jesse.services.selectors as selectors
from jesse import sync_publish
from jesse.config import config
from jesse.services.notifier import notify
from jesse.enums import order_statuses, order_flags


class Order(Model):
    # id generated by Jesse for database usage
    id = UUIDField(primary_key=True)
    trade_id = UUIDField(index=True, null=True)
    session_id = UUIDField(index=True)

    # id generated by market, used in live-trade mode
    exchange_id = CharField(null=True)
    # some exchanges might require even further info
    vars = JSONField(default={})
    symbol = CharField()
    exchange = CharField()
    side = CharField()
    type = CharField()
    flag = CharField(null=True)
    qty = FloatField()
    price = FloatField(null=True)
    status = CharField(default=order_statuses.ACTIVE)
    created_at = BigIntegerField()
    executed_at = BigIntegerField(null=True)
    canceled_at = BigIntegerField(null=True)
    role = CharField(null=True)
    submitted_via = None

    class Meta:
        from jesse.services.db import database

        database = database.db
        indexes = ((('exchange', 'symbol'), False),)

    def __init__(self, attributes: dict = None, **kwargs) -> None:
        Model.__init__(self, attributes=attributes, **kwargs)

        if attributes is None:
            attributes = {}

        for a, value in attributes.items():
            setattr(self, a, value)

        if self.created_at is None:
            self.created_at = jh.now_to_timestamp()

        if jh.is_live():
            from jesse.store import store
            self.session_id = store.app.session_id
            self.save(force_insert=True)

        if jh.is_live():
            self.notify_submission()
        if jh.is_debuggable('order_submission') or jh.is_live():
            txt = f'{"QUEUED" if self.is_queued else "SUBMITTED"} order: {self.symbol}, {self.type}, {self.side}, {self.qty}'
            if self.price:
                txt += f', ${round(self.price, 2)}'
            logger.info(txt)

        # handle exchange balance for ordered asset
        e = selectors.get_exchange(self.exchange)
        e.on_order_submission(self)

    def broadcast(self) -> None:
        sync_publish('order', self.to_dict)

    def notify_submission(self) -> None:
        self.broadcast()

        if config['env']['notifications']['events']['submitted_orders']:
            txt = f'{"QUEUED" if self.is_queued else "SUBMITTED"} order: {self.symbol}, {self.type}, {self.side}, {self.qty}'
            if self.price:
                txt += f', ${round(self.price, 2)}'
            notify(txt)

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
    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'exchange_id': self.exchange_id,
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

        if jh.is_live():
            self.save()

        if not silent:
            txt = f'CANCELED order: {self.symbol}, {self.type}, {self.side}, {self.qty}'
            if self.price:
                txt += f', ${round(self.price, 2)}'
            if jh.is_debuggable('order_cancellation') or jh.is_live():
                logger.info(txt)
            if jh.is_live():
                self.broadcast()
                if config['env']['notifications']['events']['cancelled_orders']:
                    notify(txt)

        # handle exchange balance
        e = selectors.get_exchange(self.exchange)
        e.on_order_cancellation(self)

    def execute(self, silent=False) -> None:
        if self.is_canceled or self.is_executed:
            return

        self.executed_at = jh.now_to_timestamp()
        self.status = order_statuses.EXECUTED

        if jh.is_live():
            self.save()

        if not silent:
            txt = f'EXECUTED order: {self.symbol}, {self.type}, {self.side}, {self.qty}'
            if self.price:
                txt += f', ${round(self.price, 2)}'
            # log
            if jh.is_debuggable('order_execution') or jh.is_live():
                logger.info(txt)
            # notify
            if jh.is_live():
                self.broadcast()
                if config['env']['notifications']['events']['executed_orders']:
                    notify(txt)

        p = selectors.get_position(self.exchange, self.symbol)

        if p:
            p._on_executed_order(self)

        # handle exchange balance for ordered asset
        e = selectors.get_exchange(self.exchange)
        e.on_order_execution(self)
