# Data Preprocessing Script

import pandas as pd
import glob

def process_data():
    files = glob.glob('data/raw/*.csv')
    df_list = [pd.read_csv(file, index_col=0, parse_dates=True) for file in files]
    df = pd.concat(df_list).sort_index()
    
    # Further processing, e.g., handling missing values, feature engineering
    df.fillna(method='ffill', inplace=True)
    
    df.to_csv('data/processed/processed_data.csv')

if __name__ == "__main__":
    process_data()
