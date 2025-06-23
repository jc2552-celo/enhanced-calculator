from app.operation_strategy import OperationStrategy

class AddStrategy(OperationStrategy):
    def execute(self, a, b):
        return a + b

