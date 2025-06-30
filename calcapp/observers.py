import os
import pandas as pd
from calcapp.logger import log_operation

class Observer:
    def update(self, operation, a, b, result):
        raise NotImplementedError("Subclass must implement update method")

class LoggingObserver(Observer):
    def update(self, operation, a, b, result):
        log_operation(operation, a, b, result)

class AutoSaveObserver(Observer):
    def __init__(self, filename="history/history.csv"):
        self.filename = filename
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"]).to_csv(self.filename, index=False)

    def update(self, operation, a, b, result):
        df = pd.DataFrame([[operation, a, b, result]], columns=["Operation", "Operand1", "Operand2", "Result"])
        df.to_csv(self.filename, mode="a", header=False, index=False)

