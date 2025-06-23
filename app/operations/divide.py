from app.operation_strategy import OperationStrategy

class DivideStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

