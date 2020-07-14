from jesse.strategies import Strategy


# test_on_route_open_position part 2 - ETHUSD
class Test22(Strategy):
    def should_long(self):
        """

        :return:
        """
        return self.price == 10

    def should_short(self):
        """

        :return:
        """
        return False

    def go_long(self):
        """

        """
        self.buy = 1, self.price
        self.take_profit = 1, 20

    def go_short(self):
        """

        """
        pass

    def should_cancel(self):
        """

        :return:
        """
        return False
