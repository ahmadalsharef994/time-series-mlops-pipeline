import pandas as pd
import tensorflow as tf
from statsmodels.tsa.arima.model import ARIMA
import joblib
from dotenv import load_dotenv
import os

load_dotenv()

def train():
    # Load the cleaned CSV
    df = pd.read_csv("data/raw/latest_data.csv")

    # Prepare inputs and labels
    X = df[['Open', 'High', 'Low', 'Volume']].values.astype('float32')
    y = df['Close'].values.astype('float32')

    epochs = int(os.getenv("LSTM_EPOCHS"))
    batch_size = int(os.getenv("LSTM_BATCH_SIZE"))
    order = tuple(map(int, os.getenv("ARIMA_ORDER").split(",")))

    # Train LSTM
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=epochs, batch_size=batch_size)
    model.save("models/lstm/lstm_model.h5")
    print("[Train] LSTM model trained and saved.")

    # Train ARIMA
    arima_model = ARIMA(y, order=order)
    arima_result = arima_model.fit()
    joblib.dump(arima_result, "models/arima/arima_model.pkl")
    print("[Train] ARIMA model trained and saved.")

if __name__ == "__main__":
    train()
