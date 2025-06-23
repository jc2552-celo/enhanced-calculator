from app.operation_strategy import OperationStrategy

class PowerStrategy(OperationStrategy):
    def execute(self, a, b):
        return a ** b

