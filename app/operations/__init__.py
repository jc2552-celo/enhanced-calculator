from .add_strategy import AddStrategy
from .subtract import SubtractStrategy
from .multiply import MultiplyStrategy
from .divide import DivideStrategy
from .power import PowerStrategy
from .root import RootStrategy

operations_map = {
    'add': AddStrategy,
    'subtract': SubtractStrategy,
    'multiply': MultiplyStrategy,
    'divide': DivideStrategy,
    'power': PowerStrategy,
    'root': RootStrategy
}
