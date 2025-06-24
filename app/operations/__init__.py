from app.operations.add_strategy import AddStrategy
from app.operations.subtract_strategy import SubtractStrategy
from app.operations.multiply_strategy import MultiplyStrategy
from app.operations.divide_strategy import DivideStrategy

operations_map = {
    "add": AddStrategy,
    "subtract": SubtractStrategy,
    "multiply": MultiplyStrategy,
    "divide": DivideStrategy,
}

