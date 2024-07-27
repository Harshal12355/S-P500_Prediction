# Model Training Script

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle

def train_model():
    df = pd.read_csv('data/processed/processed_data.csv', index_col=0, parse_dates=True)
    
    model = ARIMA(df['Close'], order=(5, 1, 0))
    model_fit = model.fit()
    
    with open('models/arima_model.pkl', 'wb') as f:
        pickle.dump(model_fit, f)

if __name__ == "__main__":
    train_model()
