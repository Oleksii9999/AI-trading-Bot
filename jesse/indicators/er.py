from typing import Union

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

from jesse.helpers import get_candle_source
from jesse.helpers import get_config


def er(candles: np.ndarray, period: int = 5, source_type: str = "close", sequential: bool = False) -> Union[
    float, np.ndarray]:
    """
    ER - The Kaufman Efficiency indicator

    :param candles: np.ndarray
    :param period: int - default: 5
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    warmup_candles_num = get_config('env.data.warmup_candles_num', 240)
    if not sequential and len(candles) > warmup_candles_num:
        candles = candles[-warmup_candles_num:]

    source = get_candle_source(candles, source_type=source_type)

    change = np.abs(np.diff(source, period))
    abs_dif = np.abs(np.diff(source))
    swv = sliding_window_view(abs_dif, window_shape=period)
    volatility = swv.sum()

    res = change / volatility

    return np.concatenate((np.full((candles.shape[0] - res.shape[0]), np.nan), res), axis=0) if sequential else res[-1]
