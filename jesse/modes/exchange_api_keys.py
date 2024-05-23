from typing import Optional
from starlette.responses import JSONResponse
from jesse.info import live_trading_exchanges
import jesse.helpers as jh


def get_api_keys():
    return JSONResponse({
        'data': []
    }, status_code=200)


def store_api_keys(exchange: str, name: str, api_key: str, api_secret: str, additional_fields: Optional[dict] = None):
    # validate the exchange
    if exchange not in live_trading_exchanges:
        raise ValueError(f'Invalid exchange: {exchange}')

    from jesse.services.db import database
    database.open_connection()

    from jesse.models.ExchangeApiKeys import ExchangeApiKeys

    # check if the api key already exists
    if ExchangeApiKeys.select().where(ExchangeApiKeys.name == name).exists():
        raise ValueError(f'API key with the name "{name}" already exists. Please choose another name.')

    try:
        # create the record
        ExchangeApiKeys.create(
            exchange_name=exchange,
            name=name,
            api_key=api_key,
            api_secret=api_secret,
            additional_fields=additional_fields,
            created_at=jh.now(True)
        )
    except Exception as e:
        database.close_connection()
        return JSONResponse({
            'error': str(e)
        }, status_code=500)

    database.close_connection()

    return JSONResponse({
        'message': 'API key has been stored successfully.'
    }, status_code=200)
