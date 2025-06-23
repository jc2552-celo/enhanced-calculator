from app.operation_strategy import OperationStrategy

class DivideStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

