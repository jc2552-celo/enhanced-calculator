from app.operations import Addition, Subtraction, Multiplication, Division, Power, Root
from app.calculation import Calculation

class CalculationFactory:
    @staticmethod
    def create(a: float, b: float, operator: str) -> Calculation:
        operator_map = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Power(),
            'root': Root()
        }

        if operator not in operator_map:
            raise ValueError(f"Unsupported operator: {operator}")

        return Calculation(a, b, operator_map[operator])
