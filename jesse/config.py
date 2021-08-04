config = {
    # these values are related to the user's environment
    'env': {
        'caching': {
            'driver': 'pickle'
        },

        'logging': {
            'order_submission': True,
            'order_cancellation': True,
            'order_execution': True,
            'position_opened': True,
            'position_increased': True,
            'position_reduced': True,
            'position_closed': True,
            'shorter_period_candles': False,
            'trading_candles': True,
            'balance_update': True,
        },

        'exchanges': {
            'Sandbox': {
                'fee': 0,
                'type': 'spot',
                # used only in futures trading
                'settlement_currency': 'USDT',
                # accepted values are: 'cross' and 'isolated'
                'futures_leverage_mode': 'cross',
                # 1x, 2x, 10x, 50x, etc. Enter as integers
                'futures_leverage': 1,
                'assets': [
                    {'asset': 'USDT', 'balance': 10_000},
                    {'asset': 'BTC', 'balance': 0},
                ],
            },

            # https://www.bitfinex.com
            'Bitfinex': {
                'fee': 0.002,

                # backtest mode only: accepted are 'spot' and 'futures'
                'type': 'futures',

                # futures mode only
                'settlement_currency': 'USD',
                # accepted values are: 'cross' and 'isolated'
                'futures_leverage_mode': 'cross',
                # 1x, 2x, 10x, 50x, etc. Enter as integers
                'futures_leverage': 1,

                'assets': [
                    {'asset': 'USDT', 'balance': 10_000},
                    {'asset': 'USD', 'balance': 10_000},
                    {'asset': 'BTC', 'balance': 0},
                ],
            },

            # https://www.binance.com
            'Binance': {
                'fee': 0.001,

                # backtest mode only: accepted are 'spot' and 'futures'
                'type': 'futures',

                # futures mode only
                'settlement_currency': 'USDT',
                # accepted values are: 'cross' and 'isolated'
                'futures_leverage_mode': 'cross',
                # 1x, 2x, 10x, 50x, etc. Enter as integers
                'futures_leverage': 1,

                'assets': [
                    {'asset': 'USDT', 'balance': 10_000},
                    {'asset': 'BTC', 'balance': 0},
                ],
            },

            # https://www.binance.com
            'Binance Futures': {
                'fee': 0.0004,

                # backtest mode only: accepted are 'spot' and 'futures'
                'type': 'futures',

                # futures mode only
                'settlement_currency': 'USDT',
                # accepted values are: 'cross' and 'isolated'
                'futures_leverage_mode': 'cross',
                # 1x, 2x, 10x, 50x, etc. Enter as integers
                'futures_leverage': 1,

                'assets': [
                    {'asset': 'USDT', 'balance': 10_000},
                ],
            },

            # https://testnet.binancefuture.com
            'Testnet Binance Futures': {
                'fee': 0.0004,

                # backtest mode only: accepted are 'spot' and 'futures'
                'type': 'futures',

                # futures mode only
                'settlement_currency': 'USDT',
                # accepted values are: 'cross' and 'isolated'
                'futures_leverage_mode': 'cross',
                # 1x, 2x, 10x, 50x, etc. Enter as integers
                'futures_leverage': 1,

                'assets': [
                    {'asset': 'USDT', 'balance': 10_000},
                ],
            },

            # https://pro.coinbase.com
            'Coinbase': {
                'fee': 0.005,

                # backtest mode only: accepted are 'spot' and 'futures'
                'type': 'futures',

                # futures mode only
                'settlement_currency': 'USD',
                # accepted values are: 'cross' and 'isolated'
                'futures_leverage_mode': 'cross',
                # 1x, 2x, 10x, 50x, etc. Enter as integers
                'futures_leverage': 1,

                'assets': [
                    {'asset': 'USDT', 'balance': 10_000},
                    {'asset': 'USD', 'balance': 10_000},
                    {'asset': 'BTC', 'balance': 0},
                ],
            },
        },

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Optimize mode
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #
        # Below configurations are related to the optimize mode
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        'optimization': {
            # sharpe, calmar, sortino, omega
            'ratio': 'sharpe',
        },

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        # Data
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #
        # Below configurations are related to the data
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        'data': {
            # The minimum number of warmup candles that is loaded before each session.
            'warmup_candles_num': 240,
        }
    },

    # These values are just placeholders used by Jesse at runtime
    'app': {
        # list of currencies to consider
        'considering_symbols': [],
        # The symbol to trade.
        'trading_symbols': [],

        # list of time frames to consider
        'considering_timeframes': [],
        # Which candle type do you intend trade on
        'trading_timeframes': [],

        # list of exchanges to consider
        'considering_exchanges': [],
        # list of exchanges to consider
        'trading_exchanges': [],

        'considering_candles': [],

        # dict of registered live trade drivers
        'live_drivers': {},

        # Accepted values are: 'backtest', 'livetrade', 'fitness'.
        'trading_mode': '',

        # variable used for test-driving the livetrade mode
        'is_test_driving': False,

        # this would enable many console.log()s in the code, which are helpful for debugging.
        'debug_mode': False,

        # this is only used for the live unit tests
        'is_unit_testing': False,
    },
}


def set_config(c) -> None:
    global config

    if 'logging' in c:
        config['env']['logging'] = c['logging']

    if 'warm_up_candles' in c:
        config['env']['data']['warmup_candles_num'] = int(c['warm_up_candles'])

    if 'optimization' in c:
        config['env']['optimization'] = c['optimization']

    if 'exchanges' in c:
        for e in c['exchanges']:
            config['env']['exchanges'][e['name']] = {
                'fee': float(e['fee']),
                'type': 'futures',
                # used only in futures trading
                'settlement_currency': 'USDT',
                # accepted values are: 'cross' and 'isolated'
                'futures_leverage_mode': e['futures_leverage_mode'],
                # 1x, 2x, 10x, 50x, etc. Enter as integers
                'futures_leverage': int(e['futures_leverage']),
                'assets': [
                    {'asset': 'USDT', 'balance': float(e['balance'])},
                ],
            }

    if 'notifications' in c:
        config['env']['notifications'] = c['notifications']

    # TODO: must become a config value later when we go after multi account support?
    config['env']['identifier'] = 'main'

    # # add sandbox because it isn't in the local config file but it is needed since we might have replaced it
    # config['env']['exchanges']['Sandbox'] = {
    #     'type': 'spot',
    #     # used only in futures trading
    #     'settlement_currency': 'USDT',
    #     'fee': 0,
    #     'futures_leverage_mode': 'cross',
    #     'futures_leverage': 1,
    #     'assets': [
    #         {'asset': 'USDT', 'balance': 10_000},
    #         {'asset': 'BTC', 'balance': 0},
    #     ],
    # }


def reset_config() -> None:
    global config
    config = backup_config.copy()


backup_config = config.copy()
