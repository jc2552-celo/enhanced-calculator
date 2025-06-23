class CalculationHistory:
    def __init__(self):
        self._history = []

    def add_calculation(self, calculation):
        self._history.append(str(calculation))

    def get_history(self):
        return self._history

