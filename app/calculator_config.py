from dotenv import load_dotenv
import os

load_dotenv()

# Constants
HISTORY_FILE = os.getenv("HISTORY_FILE", "data/history.csv")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")  # <-- ADD THIS

def get_history_file():
    return HISTORY_FILE
