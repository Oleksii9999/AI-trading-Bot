from jesse.strategies import Strategy


class TestCanCancelEntryOrdersAfterOpenPositionLong1(Strategy):
    def before(self) -> None:
        if self.price == 12:
            self._fake_order(0, 'MARKET', 'EXECUTED', 10)
            self._fake_order(1, 'LIMIT', 'ACTIVE', 9)
            self._fake_order(2, 'LIMIT', 'ACTIVE', 8)
        elif self.price == 15:
            self._fake_order(0, 'MARKET', 'EXECUTED', 10)
            assert self.orders[1].type == 'LIMIT'
            assert self.orders[1].status == 'CANCELED'
            assert self.orders[2].type == 'LIMIT'
            assert self.orders[2].status == 'CANCELED'

    def _fake_order(self, i, type, status, price):
        assert self.orders[i].type == type
        assert self.orders[i].status == status
        assert self.orders[i].price == price

    def should_long(self) -> bool:
        return self.price == 10

    def should_short(self) -> bool:
        return False

    def go_long(self):
        self.buy = [
            (1, 10),
            (1, 9),
            (1, 8),
        ]

    def update_position(self) -> None:
        if self.price == 13:
            self.buy = []

    def go_short(self):
        pass

    def should_cancel(self):
        return False
