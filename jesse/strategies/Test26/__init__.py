from jesse.strategies import Strategy


# test_on_route_stop_loss part 2 - ETHUSD
class Test26(Strategy):
    def should_long(self):
        """

        :return:
        """
        return False

    def should_short(self):
        """

        :return:
        """
        return self.price == 10

    def go_long(self):
        """

        """
        pass

    def go_short(self):
        """

        """
        self.sell = 1, self.price
        self.stop_loss = 1, 20

    def should_cancel(self):
        """

        :return:
        """
        return False
