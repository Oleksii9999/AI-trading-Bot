from typing import Union

import numpy as np
import talib
from scipy.ndimage.filters import maximum_filter1d, minimum_filter1d

from jesse.helpers import get_config


def chande(candles: np.ndarray, period: int = 22, mult: float = 3.0, direction: str = "long",
           sequential: bool = False) -> Union[float, np.ndarray]:
    """
    Chandelier Exits

    :param candles: np.ndarray
    :param period: int - default: 22
    :param period: float - default: 3.0
    :param direction: str - default: "long"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 240)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    candles_close = candles[:, 2]
    candles_high = candles[:, 3]
    candles_low = candles[:, 4]

    atr = talib.ATR(candles_high, candles_low, candles_close, timeperiod=period)

    if direction == 'long':
        maxp = filter1d_same(candles_high, period, 'max')
        result = maxp - atr * mult
    elif direction == 'short':
        maxp = filter1d_same(candles_low, period, 'min')
        result = maxp + atr * mult
    else:
        print('The last parameter must be \'short\' or \'long\'')

    return result if sequential else result[-1]


def filter1d_same(a: np.array, W: int, type: str, fillna=np.nan):
    out_dtype = np.full(0, fillna).dtype
    hW = (W - 1) // 2  # Half window size
    if type == 'max':
        out = maximum_filter1d(a, size=W, origin=hW)
    else:
        out = minimum_filter1d(a, size=W, origin=hW)
    if out.dtype is out_dtype:
        out[:W - 1] = fillna
    else:
        out = np.concatenate((np.full(W - 1, fillna), out[W - 1:]))
    return out
