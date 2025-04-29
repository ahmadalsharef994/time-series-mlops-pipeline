import os
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def preprocess():
    try:
        # Load environment variables
        ticker = os.getenv("DATA_SOURCE_YAHOO_TICKER", "AAPL")
        period = os.getenv("DATA_SOURCE_YAHOO_PERIOD", "7d")
        logger.info(f"Fetching data for {ticker} over {period}")

        # Fetch data
        df = yf.download(ticker, period=period, auto_adjust=True)
        if df.empty:
            raise ValueError(f"No data returned for ticker {ticker} over {period}")

        # Debug: Print initial columns
        logger.info(f"Initial columns: {list(df.columns)}")

        # Handle multi-index columns
        if isinstance(df.columns, pd.MultiIndex):
            # Extract the first level of the multi-index (column names)
            df.columns = [col[0] for col in df.columns]
        else:
            # Normalize column names for single-level index
            df.columns = [col.lower().capitalize() for col in df.columns]

        # Debug: Print normalized columns
        logger.info(f"Normalized columns: {list(df.columns)}")

        # Explicitly select columns
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise KeyError(f"Missing required columns: {missing_cols}")

        df = df[required_cols]

        # Drop NaNs and enforce numeric types
        df.dropna(inplace=True)
        df = df.astype(float)

        # Ensure data folder exists
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv("data/raw/latest_data.csv", index=True)  # Include index for time-series data

        logger.info("Data saved cleanly to data/raw/latest_data.csv")

    except Exception as e:
        logger.error(f"Error in preprocessing: {str(e)}")
        raise

if __name__ == "__main__":
    preprocess()