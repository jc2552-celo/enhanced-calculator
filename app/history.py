class HistoryManager:
    def __init__(self):
        self.history = []

    def add(self, calc):
        self.history.append(calc)

    def get_last(self):
        return self.history[-1] if self.history else None

    def clear(self):
        self.history = []

# ✅ Ensure this is defined and not commented out!

