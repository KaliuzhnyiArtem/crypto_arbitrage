import requests
from binance.client import Client


API = 'MdP6dkVlCZo9JpKhrACmL8nfgEGowlsdW9NBCyXJYcaaqY32yUmLnhFaZwfeBxGW'
SECRET_KEY = 't9qNEFIJwqTb5U0QRnaQUEm9LRwwROkf1P6vPUfIBlv1cuKzfS4jewoxQydngwwc'


# Return price symbol
def get_price(symbol):
    base = 'https://api.binance.com'
    path = '/api/v3/depth'
    url = base + path
    param = {'symbol': symbol}
    bit_price = requests.get(url, params=param).json()
    return bit_price['bids'][0]


# Return list trade pairs
def get_trade_pairs():
    ls = []
    client = Client(API, SECRET_KEY)
    exchange_info = client.get_exchange_info()
    for i in exchange_info['symbols']:
        ls.append(i['symbol'])
    return ls





