import numpy as np
from playhouse.postgres_ext import *

import jesse.helpers as jh
import jesse.services.logger as logger
import jesse.services.selectors as selectors
from jesse.config import config
from jesse.enums import order_statuses, order_flags
from jesse.services.db import db
from jesse.services.notifier import notify


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

    class Meta:
        database = db
        indexes = ((('exchange', 'symbol'), False),)

    def __init__(self, attributes=None, **kwargs) -> None:
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
                '{} order: {}, {}, {}, {}, ${}'.format(
                    'QUEUED' if self.is_queued else 'SUBMITTED',
                    self.symbol, self.type, self.side, self.qty,
                    round(self.price, 2)
                )
            )

        # handle exchange balance for ordered asset
        e = selectors.get_exchange(self.exchange)
        e.on_order_submission(self)

    def notify_submission(self) -> None:
        notify(
            '{} order: {}, {}, {}, {}, ${}'.format(
                'QUEUED' if self.is_queued else 'SUBMITTED',
                self.symbol, self.type, self.side, self.qty,
                round(self.price, 2)
            )
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

    def cancel(self) -> None:
        if self.is_canceled or self.is_executed:
            return

        self.canceled_at = jh.now_to_timestamp()
        self.status = order_statuses.CANCELED

        if jh.is_debuggable('order_cancellation'):
            logger.info(
                'CANCELED order: {}, {}, {}, {}, ${}'.format(
                    self.symbol, self.type, self.side, self.qty, round(self.price, 2)
                )
            )
        if jh.is_live() and config['env']['notifications']['events']['cancelled_orders']:
            notify(
                'CANCELED order: {}, {}, {}, {}, {}'.format(
                    self.symbol, self.type, self.side, self.qty, round(self.price, 2)
                )
            )

        # handle exchange balance
        e = selectors.get_exchange(self.exchange)
        e.on_order_cancellation(self)

    def execute(self) -> None:
        if self.is_canceled or self.is_executed:
            return

        self.executed_at = jh.now_to_timestamp()
        self.status = order_statuses.EXECUTED

        # log
        if jh.is_debuggable('order_execution'):
            logger.info(
                'EXECUTED order: {}, {}, {}, {}, ${}'.format(
                    self.symbol, self.type, self.side, self.qty, round(self.price, 2)
                )
            )
        # notify
        if jh.is_live() and config['env']['notifications']['events']['executed_orders']:
            notify(
                'EXECUTED order: {}, {}, {}, {}, {}'.format(
                    self.symbol, self.type, self.side, self.qty, round(self.price, 2)
                )
            )

        p = selectors.get_position(self.exchange, self.symbol)

        if p:
            p._on_executed_order(self)

        # handle exchange balance for ordered asset
        e = selectors.get_exchange(self.exchange)
        e.on_order_execution(self)


if not jh.is_unit_testing():
    # create the table
    Order.create_table()
