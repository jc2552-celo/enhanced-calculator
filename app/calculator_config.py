from dotenv import load_dotenv
import os

load_dotenv()

HISTORY_FILE = os.getenv("HISTORY_FILE", "data/history.csv")  # <- Match test expectation

def get_history_file():
    return HISTORY_FILE
