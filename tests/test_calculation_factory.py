import pytest
from app.calculation_factory import CalculationFactory

def test_factory_add():
    calc = CalculationFactory.create(1, 2, 'add')
    assert calc.get_result() == 3

def test_factory_subtract():
    calc = CalculationFactory.create(5, 3, 'subtract')
    assert calc.get_result() == 2

def test_factory_multiply():
    calc = CalculationFactory.create(4, 3, 'multiply')
    assert calc.get_result() == 12

def test_factory_divide():
    calc = CalculationFactory.create(8, 2, 'divide')
    assert calc.get_result() == 4

def test_factory_invalid():
    with pytest.raises(ValueError):
        CalculationFactory.create(1, 1, 'mod')
