class HistoryManager:
    def __init__(self, file_path="history.csv"):
        self.file_path = file_path
        self.history = []
        self.undo_stack = []
        self.redo_stack = []

    # (Make sure all methods in this class use self.file_path)
