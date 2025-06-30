import pytest
from calcapp.operations import Addition, Subtraction, Multiplication, Division

def test_addition():
    calc = Addition(3, 7)
    assert calc.execute() == 10

def test_subtraction():
    calc = Subtraction(10, 4)
    assert calc.execute() == 6

def test_multiplication():
    calc = Multiplication(5, 6)
    assert calc.execute() == 30

def test_division():
    calc = Division(12, 4)
    assert calc.execute() == 3

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        Division(5, 0).execute()

