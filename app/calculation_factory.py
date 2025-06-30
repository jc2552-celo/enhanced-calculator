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

    @staticmethod
    def create_from_input(input_str: str) -> Calculation:
        parts = input_str.strip().split()
        if len(parts) != 3:
            raise ValueError("Input must be in the format: operator operand1 operand2")
        operator, a, b = parts
        return CalculationFactory.create(float(a), float(b), operator)
