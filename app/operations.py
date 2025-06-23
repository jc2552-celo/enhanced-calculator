from app.operations.add import AddStrategy
from app.operations.subtract import SubtractStrategy
from app.operations.multiply import MultiplyStrategy
from app.operations.divide import DivideStrategy
from app.operations.power import PowerStrategy
from app.operations.root import RootStrategy

operations_map = {
    "add": AddStrategy,
    "subtract": SubtractStrategy,
    "multiply": MultiplyStrategy,
    "divide": DivideStrategy,
    "power": PowerStrategy,
    "root": RootStrategy
}

