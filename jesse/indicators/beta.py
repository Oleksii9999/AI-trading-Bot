from typing import Union

import numpy as np
from jesse.helpers import get_config
import talib


def beta(candles: np.ndarray, period: int = 5, sequential: bool = False) -> Union[float, np.ndarray]:
    """
    BETA - Beta

    :param candles: np.ndarray
    :param period: int - default: 5
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 210)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    res = talib.BETA(candles[:, 3], candles[:, 4], timeperiod=period)

    if sequential:
        return res
    else:
        return None if np.isnan(res[-1]) else res[-1]
