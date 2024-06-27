import json

import ccxt

from trading.coins import load_coins

binance = ccxt.binance()
coins = load_coins()

for coin in coins:
    ticker = binance.fetch_ticker(coin)

    with open(f"data/coins/{ticker['info']['symbol']}.json", 'w', encoding='utf8') as f:
        json.dump(ticker, f, indent=4)