import requests
import jesse.helpers as jh
from jesse.modes.import_candles_mode.drivers.interface import CandleExchange
from typing import Union
from jesse import exceptions
from .bybit_utils import timeframe_to_interval


class BybitUSDTPerpetualMain(CandleExchange):
    def __init__(self, name: str, rest_endpoint: str) -> None:
        from jesse.modes.import_candles_mode.drivers.Binance.BinanceSpot import BinanceSpot

        super().__init__(name=name, count=200, rate_limit_per_second=10, backup_exchange_class=BinanceSpot)
        self.endpoint = rest_endpoint

    def get_starting_time(self, symbol: str) -> int:
        dashless_symbol = jh.dashless_symbol(symbol)
        payload = {
            'category': 'linear',
            'symbol': dashless_symbol,
            'interval': 'W',
            'limit': 200,
            'start': 1514811660000
        }
        response = requests.get(self.endpoint + '/v5/market/kline', params=payload)
        self.validate_response(response)
        data = response.json()['list']
        return int(data[1][0])

    def fetch(self, symbol: str, start_timestamp: int, timeframe: str = '1m') -> Union[list, None]:
        dashless_symbol = jh.dashless_symbol(symbol)
        interval = timeframe_to_interval(timeframe)
        payload = {
            'category': 'linear',
            'symbol': dashless_symbol,
            'interval': interval,
            'start': start_timestamp,
            'limit': self.count
        }
        response = requests.get(self.endpoint + '/v5/market/kline', params=payload)
        self.validate_response(response)
        data = response.json()['list']
        return [
            {
                'id': jh.generate_unique_id(),
                'exchange': self.name,
                'symbol': symbol,
                'timeframe': timeframe,
                'timestamp': int(d[0]),
                'open': float(d[1]),
                'close': float(d[4]),
                'high': float(d[2]),
                'low': float(d[3]),
                'volume': float(d[5])
            } for d in data
        ]
