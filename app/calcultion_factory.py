from app.calculation import Calculation
from app.operations import operations_map

class CalculationFactory:
    @staticmethod
    def create_calculation(operation, a, b):
        strategy_class = operations_map.get(operation)
        if not strategy_class:
            raise ValueError(f"Unsupported operation: {operation}")
        return Calculation(strategy_class(), a, b)
