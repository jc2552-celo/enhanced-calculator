from app.calculation import Calculation  # Required for the return type

class CalculationFactory:
    @staticmethod
    def create(a: float, b: float, operator: str) -> Calculation:
        return Calculation.create(a, b, operator)

    @staticmethod
    def create_from_input(input_str: str) -> Calculation:
        try:
            parts = input_str.strip().split()
            if len(parts) != 3:
                raise ValueError("Invalid input format. Expected: operator operand1 operand2")
            operator, a, b = parts
            a = float(a)
            b = float(b)
            return Calculation.create(a, b, operator)
        except Exception as e:
            raise ValueError(f"Invalid input: {e}")
