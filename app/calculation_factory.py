from app.calculation import Calculation
from app.operations import Addition, Subtraction, Multiplication, Division, Power, Root
from app.operation_strategy import OperationStrategy

class CalculationFactory:
    @staticmethod
    def create(a: float, b: float, operator: str) -> Calculation:
        operation_map: dict[str, OperationStrategy] = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Power(),
            'root': Root()  # ✅ Add this line to support root
        }
        if operator not in operation_map:
            raise ValueError(f"Unsupported operator: {operator}")
        return Calculation(a, b, operation_map[operator])
