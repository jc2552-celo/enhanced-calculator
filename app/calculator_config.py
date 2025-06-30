from dotenv import load_dotenv
import os

load_dotenv()

def get_history_file():
    return os.getenv("HISTORY_FILE", "data/history.csv")

HISTORY_FILE = get_history_file()
