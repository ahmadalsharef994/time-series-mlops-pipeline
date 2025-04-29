import pandas as pd
import tensorflow as tf
import joblib
from sklearn.metrics import mean_squared_error
from math import sqrt

def evaluate():
    df = pd.read_csv("data/raw/latest_data.csv")
    X = df[['Open', 'High', 'Low', 'Volume']].values
    y_true = df['Close'].values

    # Load LSTM model
    lstm_model = tf.keras.models.load_model("models/lstm/lstm_model.h5")
    lstm_preds = lstm_model.predict(X).flatten()
    lstm_rmse = sqrt(mean_squared_error(y_true, lstm_preds))

    # Load ARIMA model
    arima_model = joblib.load("models/arima/arima_model.pkl")
    arima_preds = arima_model.predict(start=0, end=len(y_true)-1)
    arima_rmse = sqrt(mean_squared_error(y_true, arima_preds))

    print(f"[Evaluate] LSTM RMSE: {lstm_rmse:.4f}")
    print(f"[Evaluate] ARIMA RMSE: {arima_rmse:.4f}")

if __name__ == "__main__":
    evaluate()
