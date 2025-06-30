from app.calculation import Calculation
from app.operations import Addition, Subtraction, Multiplication, Division, Power, Root

class CalculationFactory:
    @staticmethod
    def create(a: float, b: float, operator_str: str):
        operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Power(),
            'root': Root()
        }

        if operator_str not in operations:
            raise ValueError(f"Unsupported operator: {operator_str}")

        operation = operations[operator_str]
        return Calculation(a, b, operation)

    @staticmethod
    def create_from_input(input_str: str):
        try:
            parts = input_str.strip().split()
            if len(parts) != 3:
                raise ValueError("Input must be in format: <operator> <a> <b>")

            operator_str, a_str, b_str = parts
            a = float(a_str)
            b = float(b_str)

            return CalculationFactory.create(a, b, operator_str)

        except Exception as e:
            raise ValueError(f"Invalid input: {e}")
