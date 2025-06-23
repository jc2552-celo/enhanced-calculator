from app.operation_strategy import OperationStrategy

class RootStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot take the root with exponent zero.")
        return a ** (1 / b)
