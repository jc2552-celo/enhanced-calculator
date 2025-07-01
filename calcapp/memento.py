class Caretaker:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def save(self, operation, a, b, result):
        self._history.append((operation, a, b, result))
        self._redo_stack.clear()  # Clear redo stack on new save

    def undo(self):
        if not self._history:
            return None
        state = self._history.pop()
        self._redo_stack.append(state)
        return state

    def redo(self):
        if not self._redo_stack:
            return None
        state = self._redo_stack.pop()
        self._history.append(state)
        return state

