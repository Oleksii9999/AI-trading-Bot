from collections import namedtuple

import numpy as np
import talib

from jesse.helpers import get_candle_source

MACDEXT = namedtuple('MACDEXT', ['macd', 'signal', 'hist'])


def macdext(candles: np.ndarray, fast_period: int = 12, fast_ma_type: int = 0, slow_period: int = 26,
            slow_ma_type: int = 0, signal_period: int = 9, signal_ma_type: int = 0, source_type: str = "close",
            sequential: bool = False) -> MACDEXT:
    """
    MACDEXT - MACD with controllable MA type

    :param candles: np.ndarray
    :param fast_period: int - default: 12
    :param fastma_type: int - default: 0
    :param slow_period: int - default: 26
    :param slowma_type: int - default: 0
    :param signal_period: int - default: 9
    :param signalma_type: int - default: 0
    :param source_type: str - default: "close"
    :param sequential: bool - default: False

    :return: MACDEXT(macd, signal, hist)
    """
    if not sequential and len(candles) > 240:
        candles = candles[-240:]

    source = get_candle_source(candles, source_type=source_type)
    macd, macdsignal, macdhist = talib.MACDEXT(source, fast_period=fast_period, fastma_type=fast_ma_type,
                                               slow_period=slow_period, slowma_type=slow_ma_type,
                                               signalperiod=signal_period, signalma_type=signal_ma_type)

    if sequential:
        return MACDEXT(macd, macdsignal, macdhist)
    else:
        return MACDEXT(macd[-1], macdsignal[-1], macdhist[-1])
