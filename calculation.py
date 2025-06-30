# app/calculation.py
class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = self.operation.calculate(a, b)

    def get_result(self):
        return self.result
