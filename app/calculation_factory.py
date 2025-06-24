from app.operations.add_strategy import AddStrategy
from app.operations.subtract_strategy import SubtractStrategy
from app.operations.multiply_strategy import MultiplyStrategy
from app.operations.divide_strategy import DivideStrategy

operations_map = {
    "add": AddStrategy,
    "subtract": SubtractStrategy,
    "multiply": MultiplyStrategy,
    "divide": DivideStrategy
}

class CalculationFactory:
    @staticmethod
    def create(a, b, operation):
        if operation not in operations_map:
            raise KeyError(f"Unsupported operation: {operation}")
        strategy_class = operations_map[operation]
        strategy = strategy_class()
        return strategy.calculate(a, b)

