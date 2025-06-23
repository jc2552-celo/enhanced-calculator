from app.operation_strategy import OperationStrategy

class RootStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot take zeroth root.")
        return a ** (1 / b)

