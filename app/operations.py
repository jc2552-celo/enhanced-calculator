from abc import ABC, abstractmethod

# Strategy Interface
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

# Concrete Strategies
class Addition(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtraction(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a - b

class Multiplication(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a * b

class Division(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

class Power(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a ** b

class Root(OperationStrategy):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Zeroth root is undefined.")
        return a ** (1 / b)
