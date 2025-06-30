import pandas as pd

class CalculatorMemento:
    def __init__(self, state: pd.DataFrame):
        self._state = state.copy(deep=True)

    def get_state(self) -> pd.DataFrame:
        return self._state.copy(deep=True)
