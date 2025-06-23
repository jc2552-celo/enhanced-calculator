from app.operations import operations_map
from app.calculation import Calculation

class CalculationFactory:
    @staticmethod
    def create(operation, a, b):
        if operation not in operations_map:
            raise KeyError(f"Unsupported operation: {operation}")
        strategy = operations_map[operation]()
        return Calculation(a, b, strategy)

