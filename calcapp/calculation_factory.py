from calcapp.operations import Addition, Subtraction, Multiplication, Division
from calcapp.exceptions import OperationError

class CalculationFactory:
    @staticmethod
    def create(operation, a, b):
        if operation == "add":
            return Addition(a, b)
        elif operation == "subtract":
            return Subtraction(a, b)
        elif operation == "multiply":
            return Multiplication(a, b)
        elif operation == "divide":
            return Division(a, b)
        else:
            raise OperationError(f"Unsupported operation: {operation}")

