import pandas as pd
import yfinance as yf

def fetch_data(symbol, interval='1d', period='6mo'):
    data = yf.download(symbol, interval=interval, period=period)
    data.dropna(inplace=True)
    return data
