from app.operation_strategy import OperationStrategy

class MultiplyStrategy(OperationStrategy):
    def execute(self, a, b):
        return a * b
