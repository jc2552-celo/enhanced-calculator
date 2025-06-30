import pytest
from app.operations import Addition, Subtraction, Multiplication, Division, Power, Root

def test_addition():
    assert Addition().execute(5, 3) == 8

def test_subtraction():
    assert Subtraction().execute(5, 3) == 2

def test_multiplication():
    assert Multiplication().execute(5, 3) == 15

def test_division():
    assert Division().execute(10, 2) == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division().execute(10, 0)

def test_power():
    assert Power().execute(2, 3) == 8

def test_root():
    assert Root().execute(27, 3) == 3

def test_zeroth_root():
    with pytest.raises(ValueError):
        Root().execute(27, 0)
