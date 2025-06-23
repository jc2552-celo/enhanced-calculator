from .calculation import Calculation
from app.operations import add, subtract, multiply, divide

class CalculationFactory:
    operations_map = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    @staticmethod
    def create(operand1, operand2, operation_name):
        operation = CalculationFactory.operations_map.get(operation_name)
        if not operation:
            raise ValueError(f"Invalid operation: {operation_name}")
        return Calculation(operand1, operand2, operation)
