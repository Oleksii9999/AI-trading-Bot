from jesse.config import config
from jesse.enums import exchanges, timeframes
from jesse.routes import router
from jesse.store import store


def test_routes():
    # re-define routes
    router.set_routes([
        (exchanges.BITFINEX, 'ETHUSD', timeframes.HOUR_3, 'Test19'),
        (exchanges.SANDBOX, 'BTCUSD', timeframes.MINUTE_15, 'Test19'),
    ])

    router.set_extra_candles([
        (exchanges.BITFINEX, 'EOSUSD', timeframes.HOUR_3),
        (exchanges.BITFINEX, 'EOSUSD', timeframes.HOUR_1),
    ])

    # reset store for new routes to take affect
    store.reset(True)

    # now assert it's working as expected
    assert set(config['app']['trading_exchanges']) == set([exchanges.SANDBOX, exchanges.BITFINEX])
    assert set(config['app']['trading_symbols']) == set(['BTCUSD', 'ETHUSD'])
    assert set(config['app']['trading_timeframes']) == set([timeframes.HOUR_3, timeframes.MINUTE_15])
    assert set(config['app']['considering_exchanges']) == set([exchanges.SANDBOX, exchanges.BITFINEX])
    assert set(config['app']['considering_symbols']) == set(['BTCUSD', 'ETHUSD', 'EOSUSD'])
    assert set(config['app']['considering_timeframes']) == set(
        [timeframes.MINUTE_1, timeframes.HOUR_3, timeframes.MINUTE_15, timeframes.HOUR_1])
