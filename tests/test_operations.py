from app.operations.add_strategy import AddStrategy
from app.operations.subtract import SubtractStrategy
from app.operations.multiply import MultiplyStrategy
from app.operations.divide import DivideStrategy

def test_add():
    assert AddStrategy().calculate(2, 3) == 5
    assert AddStrategy().calculate(-1, 1) == 0
    assert AddStrategy().calculate(0, 0) == 0

def test_subtract():
    assert SubtractStrategy().calculate(5, 2) == 3
    assert SubtractStrategy().calculate(10, 10) == 0
    assert SubtractStrategy().calculate(0, 5) == -5

def test_multiply():
    assert MultiplyStrategy().calculate(3, 4) == 12
    assert MultiplyStrategy().calculate(0, 5) == 0
    assert MultiplyStrategy().calculate(-2, 3) == -6

def test_divide():
    assert DivideStrategy().calculate(10, 2) == 5
    assert DivideStrategy().calculate(9, 3) == 3
    assert DivideStrategy().calculate(5, 2) == 2.5

