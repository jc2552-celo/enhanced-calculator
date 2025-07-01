import pytest
from calcapp.operations import Addition, Subtraction, Multiplication, Division

def test_addition():
    assert Addition(2, 3).execute() == 5

def test_subtraction():
    assert Subtraction(5, 3).execute() == 2

def test_multiplication():
    assert Multiplication(4, 3).execute() == 12

def test_division():
    assert Division(10, 2).execute() == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division(5, 0).execute()

