# scripts/data_collection.py

import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_data():
    ticker = "SPY"
    data = yf.download(ticker, interval="1m", period="1d")
    
    data.to_csv(f'data/raw/{datetime.now().strftime("%Y%m%d_%H%M%S")}_s&p500_data.csv')

if __name__ == "__main__":
    fetch_data()
