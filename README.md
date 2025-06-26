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

```

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


## Installation
1. Ensure Docker and Python 3.x are installed.
2. Clone the repository: `git clone https://github.com/ahmadalsharef994/time-series-mlops-pipeline.git`
3. Build the Docker image: `docker build -t time-series-mlops .`
4. Install dependencies: `pip install -r requirements.txt` (if running locally).

## Usage
1. Start the services: `docker-compose up`
2. Access the API at `http://localhost:8000/predict`
3. Example request: `curl -X POST -d '{"data": [1, 2, 3]}' http://localhost:8000/predict`

## Project Structure
- `data_processing/`: Scripts for data cleaning and preparation
- `model/`: Model training and evaluation logic
- `deployment/`: Configuration for serving the model
- `Dockerfile`: Docker setup

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue.

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
