import json

import ccxt
import pandas as pd

binance = ccxt.binance()


def load_coins():
    with open("data/markets.json", "r", encoding='utf8') as file_reader:
        return json.load(file_reader)
    

def save_coins():
    markets = binance.load_markets()

    with open("data/markets.json", "w", encoding='utf8') as file_writer:
        json.dump(markets, file_writer, indent=4)