from app.history import History
from app.calculation_factory import CalculationFactory

class CalculatorFacade:
    def __init__(self):
        self.history_manager = History()
        self.history = self.history_manager.history

    def execute_command(self, input_str):
        try:
            calculation = CalculationFactory.create_from_input(input_str)
            result = calculation.perform()
            print(f"Result: {result}")
            self.history_manager.add_to_history(input_str, result)
            self.history = self.history_manager.history
        except Exception as e:
            print(f"Input error: {e}")

def repl():
    print("Welcome to Enhanced Calculator!")
    calc = CalculatorFacade()
    while True:
        user_input = input("Enter command (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        calc.execute_command(user_input)

if __name__ == "__main__":
    repl()
