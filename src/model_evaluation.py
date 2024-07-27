import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluate_model():
    # Load test data
    df = pd.read_csv('data/processed/processed_data.csv', index_col=0, parse_dates=True)
    test_data = df['Close'][-100:]  # Last 100 points as test data
    
    # Load the trained model
    with open('models/arima_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Generate predictions
    predictions = model.forecast(steps=100)
    
    # Calculate evaluation metrics
    mse = mean_squared_error(test_data, predictions)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(test_data, predictions)
    
    # Save evaluation results
    eval_results = pd.DataFrame({
        'Metric': ['MSE', 'RMSE', 'MAE'],
        'Value': [mse, rmse, mae]
    })
    
    eval_results.to_csv('data/evaluation/evaluation_results.csv', index=False)
    
    print(f'MSE: {mse}')
    print(f'RMSE: {rmse}')
    print(f'MAE: {mae}')

if __name__ == "__main__":
    evaluate_model()
