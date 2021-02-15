from typing import Union

import numpy as np
from jesse.helpers import get_config
import talib

from jesse.helpers import get_candle_source


def t3(candles: np.ndarray, period: int = 5, vfactor: float = 0, source_type: str = "close",
       sequential: bool = False) -> Union[float, np.ndarray]:
    """
    T3 - Triple Exponential Moving Average (T3)

    :param candles: np.ndarray
    :param period: int - default: 5
    :param vfactor: float - default: 0
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 210)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    source = get_candle_source(candles, source_type=source_type)
    res = talib.T3(source, timeperiod=period, vfactor=vfactor)

    return res if sequential else res[-1]
