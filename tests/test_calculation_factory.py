import pytest
from app.calculation_factory import CalculationFactory

def test_factory_addition():
    calc = CalculationFactory.create(10, 5, '+')
    assert calc.perform() == 15

def test_factory_power():
    calc = CalculationFactory.create(2, 3, '^')
    assert calc.perform() == 8

def test_factory_root():
    calc = CalculationFactory.create(27, 3, 'root')
    assert round(calc.perform(), 5) == 3

def test_factory_invalid_operator():
    with pytest.raises(ValueError):
        CalculationFactory.create(5, 2, 'invalid')
