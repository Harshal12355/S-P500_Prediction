# Model Prediction Script

import pandas as pd
import pickle

def make_predictions():
    with open('models/arima_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # For simplicity, predict next 10 time steps
    predictions = model.forecast(steps=10)
    
    print(predictions)

if __name__ == "__main__":
    make_predictions()
