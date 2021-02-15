from collections import namedtuple

import numpy as np
import talib

from jesse.helpers import get_config

StochasticFast = namedtuple('StochasticFast', ['k', 'd'])


def stochf(candles: np.ndarray, fastk_period: int = 5, fastd_period: int = 3, fastd_matype: int = 0,
           sequential: bool = False) -> StochasticFast:
    """
    Stochastic Fast

    :param candles: np.ndarray
    :param fastk_period: int - default=5
    :param fastd_period: int - default=3
    :param fastd_matype: int - default=0
    :param sequential: bool - default=False

    :return: StochasticFast(k, d)
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 210)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    k, d = talib.STOCHF(
        candles[:, 3],
        candles[:, 4],
        candles[:, 2],
        fastk_period=fastk_period,
        fastd_period=fastd_period,
        fastd_matype=fastd_matype
    )

    if sequential:
        return StochasticFast(k, d)
    else:
        return StochasticFast(k[-1], d[-1])
