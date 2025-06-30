from app.calculator_repl import CalculatorFacade

def test_addition_to_history():
    calc = CalculatorFacade()
    initial_length = len(calc.history)
    calc.execute_command("+ 10 5")
    assert len(calc.history) == initial_length + 1
    assert calc.history.iloc[-1]["result"] == 15.0  # lowercase 'result'


def test_multiplication_to_history():
    calc = CalculatorFacade()
    initial_length = len(calc.history)
    calc.execute_command("* 3 4")
    assert len(calc.history) == initial_length + 1
    assert calc.history.iloc[-1]["result"] == 12.0  # lowercase 'result'
