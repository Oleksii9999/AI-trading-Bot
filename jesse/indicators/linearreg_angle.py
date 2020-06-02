from typing import Union

import numpy as np
import talib

from jesse.helpers import get_candle_source


def linearreg_angle(candles: np.ndarray, period=14, source_type="close", sequential=False) -> Union[float, np.ndarray]:
    """
    LINEARREG_ANGLE - Linear Regression Angle

    :param candles: np.ndarray
    :param period: int - default: 30
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    if not sequential and len(candles) > 240:
        candles = candles[-240:]

    source = get_candle_source(candles, source_type=source_type)
    res = talib.LINEARREG_ANGLE(source, timeperiod=period)

    return res if sequential else res[-1]
