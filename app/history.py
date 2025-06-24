class HistoryManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.history = []
        self.redo_stack = []

    def add_entry(self, operation, a, b, result):
        self.history.append((operation, a, b, result))
        self.redo_stack.clear()

    def save_history(self):
        with open(self.file_path, 'w') as f:
            for entry in self.history:
                f.write(','.join(map(str, entry)) + '\n')

    def load_history(self):
        try:
            with open(self.file_path, 'r') as f:
                self.history = [tuple(line.strip().split(',')) for line in f]
        except FileNotFoundError:
            self.history = []

    def undo(self):
        if self.history:
            last_entry = self.history.pop()
            self.redo_stack.append(last_entry)

    def redo(self):
        if self.redo_stack:
            self.history.append(self.redo_stack.pop())

    def clear(self):
        self.history.clear()
        self.redo_stack.clear()

