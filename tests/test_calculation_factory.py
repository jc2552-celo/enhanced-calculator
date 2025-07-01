import pytest
from calcapp.calculation_factory import CalculationFactory
from calcapp.exceptions import OperationError

def test_create_addition():
    result = CalculationFactory.create("add", 4, 6).execute()
    assert result == 10

def test_create_power():
    result = CalculationFactory.create("power", 2, 3).execute()
    assert result == 8

def test_create_root():
    result = CalculationFactory.create("root", 27, 3).execute()
    assert round(result, 5) == 3.0

def test_invalid_operation():
    with pytest.raises(OperationError):
        CalculationFactory.create("not_valid", 1, 2)

