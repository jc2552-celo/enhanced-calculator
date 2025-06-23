from app.operation_strategy import OperationStrategy

class SubtractStrategy(OperationStrategy):
    def execute(self, a, b):
        return a - b

