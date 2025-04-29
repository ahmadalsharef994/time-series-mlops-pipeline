import schedule
import time
from pipelines.preprocess import preprocess
from pipelines.train import train
from pipelines.evaluate import evaluate

def run_pipeline():
    print("[Pipeline] Starting full pipeline...")
    preprocess()
    train()
    evaluate()
    print("[Pipeline] Pipeline completed successfully.\n")

# Schedule the pipeline to run every day at 2:00 AM
schedule.every().day.at("02:00").do(run_pipeline)

if __name__ == "__main__":
    print("[Scheduler] Started pipeline scheduler...")
    run_pipeline()  # Run once immediately on startup
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
