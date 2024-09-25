
[![PyPI](https://img.shields.io/pypi/v/jesse)](https://pypi.org/project/jesse)
[![Downloads](https://pepy.tech/badge/jesse)](https://pepy.tech/project/jesse)
[![Docker Pulls](https://img.shields.io/docker/pulls/salehmir/jesse)](https://hub.docker.com/r/salehmir/jesse)
[![GitHub](https://img.shields.io/github/license/jesse-ai/jesse)](https://github.com/jesse-ai/jesse)
[![coverage](https://codecov.io/gh/jesse-ai/jesse/graph/badge.svg)](https://codecov.io/gh/jesse-ai/jesse)

---

## Resources

- [⚡️ Website](https://jesse.trade)
- [🎓 Documentation](https://docs.jesse.trade)
- [🎥 Youtube channel (screencast tutorials)](https://jesse.trade/youtube)
- [🛟 Help center](https://jesse.trade/help)
- [💬 Discord community](https://jesse.trade/discord)

## Screenshots

Here are a few screenshots just to get you excited:

**Backtest results:**

![image](assets/screenshots/quantstats.png)

**Example strategy code:**

```py
class SMACrossover(Strategy):
    @property
    def slow_sma(self):
        return ta.sma(self.candles, 200)

    @property
    def fast_sma(self):
        return ta.sma(self.candles, 50)

    def should_long(self) -> bool:
        # Fast SMA above Slow SMA
        return self.fast_sma > self.slow_sma

    def should_short(self) -> bool:
        # Fast SMA below Slow SMA
        return self.fast_sma < self.slow_sma

    def should_cancel_entry(self) -> bool:
        return False

    def go_long(self):
        # Open long position and use entire balance to buy
        qty = utils.size_to_qty(self.balance, self.price, fee_rate=self.fee_rate)

        self.buy = qty, self.price

    def go_short(self):
        # Open short position and use entire balance to sell
        qty = utils.size_to_qty(self.balance, self.price, fee_rate=self.fee_rate)

        self.sell = qty, self.price

    def update_position(self):
        # If there exist long position, but the signal shows Death Cross, then close the position, and vice versa.
        if self.is_long and self.fast_sma < self.slow_sma:
            self.liquidate()
    
        if self.is_short and self.fast_sma > self.slow_sma:
            self.liquidate()
```

**Live trading (requires [live plugin](https://docs.jesse.trade/docs/livetrade.html)):**

![image](assets/screenshots/live-mode.jpg)

## Disclaimer
This software is for educational purposes only. USE THE SOFTWARE AT **YOUR OWN RISK**. THE AUTHORS AND ALL AFFILIATES ASSUME **NO RESPONSIBILITY FOR YOUR TRADING RESULTS**. **Do not risk money that you are afraid to lose**. There might be **bugs** in the code - this software DOES NOT come with **ANY warranty**.
