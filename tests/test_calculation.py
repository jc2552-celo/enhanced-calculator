from app.calculation_factory import CalculationFactory

def test_calculation_factory_add():
    calc = CalculationFactory.create(2, 3, "add")
    assert calc.get_result() == 5

def test_calculation_factory_subtract():
    calc = CalculationFactory.create(5, 2, "subtract")
    assert calc.get_result() == 3

def test_calculation_factory_multiply():
    calc = CalculationFactory.create(4, 2, "multiply")
    assert calc.get_result() == 8

def test_calculation_factory_divide():
    calc = CalculationFactory.create(10, 2, "divide")
    assert calc.get_result() == 5

def test_calculation_factory_invalid_operation():
    try:
        CalculationFactory.create(2, 3, "power")  # Not a supported operation
    except ValueError as e:
        assert str(e) == "Invalid operation: power"

def test_calculation_factory_invalid_operation_numeric():
    try:
        CalculationFactory.create(2, 3, "2")  # Invalid name passed as string
    except ValueError as e:
        assert str(e) == "Invalid operation: 2"

