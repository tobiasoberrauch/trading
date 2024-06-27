import json

import ccxt

binance = ccxt.binance()

markets = binance.load_markets()

with open("data/markets.json", 'w', encoding='utf8') as f:
    json.dump(markets, f, indent=4)
