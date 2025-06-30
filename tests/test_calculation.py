from app.calculation import Calculation
from app.operations import Addition, Division

def test_perform_addition():
    calc = Calculation(5, 3, Addition())
    result = calc.perform()
    assert result == 8
    assert str(calc) == "Calculation: 5 Addition 3 = 8"

def test_perform_division():
    calc = Calculation(10, 2, Division())
    result = calc.perform()
    assert result == 5
