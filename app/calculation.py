from app.operations import OperationStrategy

class Calculation:
    def __init__(self, a: float, b: float, operation: OperationStrategy):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = None

    def perform(self):
        self.result = self.operation.execute(self.a, self.b)
        return self.result

    def __str__(self):
        return f"Calculation: {self.a} {self.operation.__class__.__name__} {self.b} = {self.result}"
