import requests

BINANCE_API = "https://api.binance.com"

def fetch_trading_pairs():
    response = requests.get(f"{BINANCE_API}/api/v3/exchangeInfo")
    response.raise_for_status()
    
    pairs = []
    for symbol in response.json()['symbols']:
        if symbol['quoteAsset'] == 'BTC' or symbol['symbol'] == 'BTCUSDT':
            pairs.append(symbol['symbol'])
    return pairs

def fetch_klines(pair, interval, start_str=None):
    payload = {'symbol': pair, 'interval': interval}
    if start_str:
        payload['startTime'] = start_str

    response = requests.get(f"{BINANCE_API}/api/v3/klines", params=payload)
    response.raise_for_status()
    return response.json()
