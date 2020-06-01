import numpy as np
import talib
from jesse.helpers import get_candle_source
from typing import Union


def tsi(candles: np.ndarray, long_period=25, short_period=13, source_type="close", sequential=False) -> Union[float, np.ndarray]:
    """
     True strength index (TSI)

    :param candles: np.ndarray
    :param long_period: int - default: 14
    :param short_period: int - default: 14
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    if not sequential and len(candles) > 240:
        candles = candles[-240:]

    source = get_candle_source(candles, source_type=source_type)
    r = 100 * (talib.EMA((talib.EMA(talib.MOM(source, 1), long_period)), short_period)) / (talib.EMA((talib.EMA(np.absolute(talib.MOM(source, 1)), long_period)), short_period))


    return r if sequential else r[-1]


