import pandas as pd
import os

class HistoryManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.DataFrame(columns=["Operation", "A", "B", "Result"])
