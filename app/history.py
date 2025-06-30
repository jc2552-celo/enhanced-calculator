from datetime import datetime
import pandas as pd

class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(columns=["timestamp", "operation", "result"])
        self.load_previous_history()

    def load_previous_history(self):
        try:
            self.history = pd.read_csv("data/history.csv")
        except FileNotFoundError:
            pass

    def add_to_history(self, operation_str, result):
        new_row = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation_str,
            "result": result
        }
        self.history = pd.concat([self.history, pd.DataFrame([new_row])], ignore_index=True)
        self.save_history()

    def save_history(self):
        self.history.to_csv("data/history.csv", index=False)
