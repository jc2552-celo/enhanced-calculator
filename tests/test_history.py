from app.calculator_repl import CalculatorFacade

def test_addition_to_history():
    calc = CalculatorFacade()
    initial_length = len(calc.history)
    calc.execute_command("+ 10 5")
    assert len(calc.history) == initial_length + 1
    assert calc.history.iloc[-1]["Result"] == 15.0

def test_multiplication_to_history():
    calc = CalculatorFacade()
    initial_length = len(calc.history)
    calc.execute_command("* 3 4")
    assert len(calc.history) == initial_length + 1
    assert calc.history.iloc[-1]["Result"] == 12.0

def test_invalid_command_does_not_add_to_history():
    calc = CalculatorFacade()
    initial_length = len(calc.history)
    calc.execute_command("invalid input")
    assert len(calc.history) == initial_length
