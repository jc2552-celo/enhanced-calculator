from app.calculation import Calculation
from app.operations import Addition, Subtraction, Multiplication, Division, Power, Root

class CalculationFactory:
    @staticmethod
    def create(a: float, b: float, operator: str) -> Calculation:
        operation_map = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Power(),
            'sqrt': Root()
        }

        if operator not in operation_map:
            raise ValueError(f"Unsupported operator: {operator}")

        operation = operation_map[operator]
        return Calculation.create(a, b, operation)

    @staticmethod
    def create_from_input(input_str: str) -> Calculation:
        parts = input_str.strip().split()

        if len(parts) != 3:
            raise ValueError("Invalid input format. Use: operator operand1 operand2")

        operator, a_str, b_str = parts
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            raise ValueError("Operands must be numbers.")

        return CalculationFactory.create(a, b, operator)
