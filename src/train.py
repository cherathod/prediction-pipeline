import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

import logging

# Configure logging
logging.basicConfig(filename='logs/model.log', level=logging.INFO)

def log_performance(model, X_test, y_test):
    score = model.score(X_test, y_test)
    logging.info(f"Model performance: R^2 Score: {score}")


def train_model(data_path, model_path):
    data = pd.read_csv(data_path)
    X = data[['Open', 'High', 'Low', 'Moving_Avg']]
    y = data['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    pickle.dump(model, open(model_path, 'wb'))
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model('data/processed_data.csv', 'models/model.pkl')
