from dotenv import load_dotenv
import os

load_dotenv()

def get_history_file():
    return os.getenv("HISTORY_FILE", "calc_history.csv")
