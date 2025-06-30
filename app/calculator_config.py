from dotenv import load_dotenv
import os

load_dotenv()

# Define this constant to match the test expectation
HISTORY_FILE = os.getenv("HISTORY_FILE", "data/history.csv")

def get_history_file():
    return HISTORY_FILE
