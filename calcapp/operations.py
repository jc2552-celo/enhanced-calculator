class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        raise NotImplementedError()

class Addition(Operation):
    def execute(self):
        return self.a + self.b

class Subtraction(Operation):
    def execute(self):
        return self.a - self.b

class Multiplication(Operation):
    def execute(self):
        return self.a * self.b

class Division(Operation):
    def execute(self):
        if self.b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self.a / self.b

class Power(Operation):
    def execute(self):
        return self.a ** self.b

class Root(Operation):
    def execute(self):
        return self.a ** (1 / self.b)

