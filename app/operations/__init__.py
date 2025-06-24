from app.operations.add_strategy import AddStrategy
from app.operations.subtract_strategy import SubtractStrategy
from app.operations.multiply_strategy import MultiplyStrategy
from app.operations.divide_strategy import DivideStrategy

operations_map = {
    "add": lambda a, b: AddStrategy().calculate(a, b),
    "subtract": lambda a, b: SubtractStrategy().calculate(a, b),
    "multiply": lambda a, b: MultiplyStrategy().calculate(a, b),
    "divide": lambda a, b: DivideStrategy().calculate(a, b),
}

