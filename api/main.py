from fastapi import FastAPI, Query
import pandas as pd
import tensorflow as tf
import joblib
from sklearn.metrics import mean_squared_error
from math import sqrt

app = FastAPI(title="Time Series Model API", description="LSTM and ARIMA models with evaluation.", version="1.0")

# Load models at startup
lstm_model = tf.keras.models.load_model("models/lstm/lstm_model.h5")
arima_model = joblib.load("models/arima/arima_model.pkl")

# Load data for evaluation
data = pd.read_csv("data/raw/latest_data.csv")
X = data[['Open', 'High', 'Low', 'Volume']].values
y_true = data['Close'].values

# Calculate RMSE once at startup
lstm_preds = lstm_model.predict(X).flatten()
lstm_rmse = sqrt(mean_squared_error(y_true, lstm_preds))

arima_preds = arima_model.predict(start=0, end=len(y_true)-1)
arima_rmse = sqrt(mean_squared_error(y_true, arima_preds))

@app.get("/", tags=["Welcome"])
def read_root():
    return {"message": "Welcome to Time Series Models API!"}

@app.get("/predict/lstm", tags=["Prediction"], summary="Predict using LSTM model")
def predict_lstm(
    open: float = Query(..., description="Open price"),
    high: float = Query(..., description="High price"),
    low: float = Query(..., description="Low price"),
    volume: float = Query(..., description="Volume traded")
):
    input_data = [[open, high, low, volume]]
    prediction = lstm_model.predict(input_data).flatten()[0]
    return {"model": "LSTM", "predicted_close": round(float(prediction), 2)}

@app.get("/predict/arima", tags=["Prediction"], summary="Predict using ARIMA model")
def predict_arima(
    index: int = Query(..., description="Index in the time series to predict")
):
    prediction = arima_model.predict(start=index, end=index)[0]
    return {"model": "ARIMA", "predicted_close": round(float(prediction), 2)}

@app.get("/evaluate/lstm", tags=["Evaluation"], summary="LSTM Model Evaluation")
def evaluate_lstm():
    return {"model": "LSTM", "RMSE": round(float(lstm_rmse), 4)}

@app.get("/evaluate/arima", tags=["Evaluation"], summary="ARIMA Model Evaluation")
def evaluate_arima():
    return {"model": "ARIMA", "RMSE": round(float(arima_rmse), 4)}
