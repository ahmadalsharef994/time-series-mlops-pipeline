# Time Series MLOps Pipeline 📈⚙️

This repository contains a complete, automated **MLOps pipeline** for **time-series forecasting**, featuring LSTM and ARIMA models. It fetches real-time financial data from Yahoo Finance, retrains models incrementally, evaluates their performance, and serves predictions through a FastAPI API.

---

## 🌟 Features

- **Automated Pipeline**: Daily fetching, training, evaluation
- **Models Included**: LSTM (TensorFlow), ARIMA (statsmodels)
- **Data Source**: Yahoo Finance via `yfinance`
- **API Serving**: FastAPI with organized Swagger UI
- **Dockerized**: Easy deployment with Docker Compose
- **Logging**: Robust logging and error handling
- **Configurable**: Fully managed via environment variables

---

## 🗂 Project Structure

```bash
.
├── api/
│   └── main.py                 # FastAPI API server
├── data/                       # Raw & processed data
├── models/                     # Saved ML models
│   ├── arima/
│   └── lstm/
├── pipelines/                  # Pipeline scripts
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── .env                        # Environment variables
├── main_pipeline.py            # Scheduler script
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## How to Run

1. Clone the repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set environment variables in `.env`:
    ```bash
    DATA_SOURCE_YAHOO_TICKER=AAPL
    DATA_SOURCE_YAHOO_PERIOD=7d
    LSTM_EPOCHS=5
    LSTM_BATCH_SIZE=32
    ARIMA_ORDER=5,1,0
    ```
4. Run the main pipeline:
    ```bash
    python main_pipeline.py
    ```
    (It will automatically run daily at 2:00 AM.)

---

## Requirements

- Python 3.8+
- Docker (optional, if you want to containerize later)

---

## Future Improvements

- Add FastAPI endpoints for real-time model querying
- Add metrics tracking and monitoring (e.g., Prometheus)
- Add cloud deployment (e.g., AWS EC2 + S3 storage)

---

## Author

- Ahmad https://github.com/ahmadalsharef994
