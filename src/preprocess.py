import pandas as pd

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    # Basic preprocessing: Fill missing values, calculate moving averages, etc.
    data['Moving_Avg'] = data['Close'].rolling(window=5).mean()
    data.dropna(inplace=True)
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data('data/raw_data.csv', 'data/processed_data.csv')
