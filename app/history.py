import pandas as pd
from datetime import datetime

class History:
    def __init__(self):
        self.history = pd.DataFrame(columns=["timestamp", "operation", "result"])

    def add(self, operation_str: str, result: float):
        new_row = {
            "timestamp": datetime.now(),
            "operation": operation_str,
            "result": result  # ✅ lowercase key
        }
        self.history = pd.concat([self.history, pd.DataFrame([new_row])], ignore_index=True)

    def __len__(self):
        return len(self.history)

    def __str__(self):
        return self.history.to_string(index=False)
