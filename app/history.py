import pandas as pd

class HistoryManager:
    def __init__(self, file_path="history.csv"):
        self.file_path = file_path
        try:
            self.df = pd.read_csv(file_path)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])
        self.undo_stack = []
        self.redo_stack = []

    def add_entry(self, operation, a, b, result):
        entry = {"operation": operation, "a": a, "b": b, "result": result}
        self.df = pd.concat([self.df, pd.DataFrame([entry])], ignore_index=True)
        self.undo_stack.append(self.df.copy())
        self.redo_stack.clear()

    def save_history(self):
        self.df.to_csv(self.file_path, index=False)

    def load_history(self):
        self.df = pd.read_csv(self.file_path)

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.df.copy())
            self.df = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.df.copy())
            self.df = self.redo_stack.pop()

    def clear(self):
        self.undo_stack.append(self.df.copy())
        self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])
        self.redo_stack.clear()

