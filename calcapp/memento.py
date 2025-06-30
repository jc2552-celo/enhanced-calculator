class Memento:
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(Memento(state))
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            return None
        memento = self._undo_stack.pop()
        self._redo_stack.append(memento)
        return memento.get_saved_state()

    def redo(self):
        if not self._redo_stack:
            return None
        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)
        return memento.get_saved_state()

    def get_history(self):
        return [m.get_saved_state() for m in self._undo_stack]

