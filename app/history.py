import pandas as pd
from datetime import datetime
import os

class HistoryManager:
    def __init__(self, file_path="data/history.csv"):
        self.file_path = file_path
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        return pd.DataFrame(columns=["timestamp", "operation", "result"])

    def add_to_history(self, operation, result):
        timestamp = datetime.now().isoformat()
        new_entry = pd.DataFrame([{
            "timestamp": timestamp,
            "operation": operation,
            "result": result
        }])
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.history.to_csv(self.file_path, index=False)
