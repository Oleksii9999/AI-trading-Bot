from typing import Union

import numpy as np
from jesse.helpers import get_config
import talib

from jesse.helpers import get_candle_source


def cfo(candles: np.ndarray, period: int = 14, scalar: float = 100, source_type: str = "close", sequential: bool = False) -> Union[
    float, np.ndarray]:
    """
    CFO - Chande Forcast Oscillator

    :param candles: np.ndarray
    :param period: int - default=14
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 210)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    source = get_candle_source(candles, source_type=source_type)

    cfo = scalar * (source - talib.LINEARREG(source, timeperiod=period))
    cfo /= source


    if sequential:
        return cfo
    else:
        return None if np.isnan(cfo[-1]) else cfo[-1]
