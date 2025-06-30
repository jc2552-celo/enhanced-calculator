from dotenv import load_dotenv
import os

load_dotenv()

HISTORY_FILE = os.getenv("HISTORY_FILE", "data/history.csv")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
ALLOWED_OPERATIONS = ["add", "subtract", "multiply", "divide", "power", "sqrt"]  # <-- Add this
