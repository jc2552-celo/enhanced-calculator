from app.calculation.calculation import Calculation
from app.operations import operations_map

class CalculationFactory:
    @staticmethod
    def create(a, b, operation):
        if operation not in operations_map:
            raise KeyError(f"Unsupported operation: {operation}")
        strategy_class = operations_map[operation]
        strategy = strategy_class()
        return Calculation(a, b, strategy)

