import pandas as pd
import os
from app.calculation_factory import CalculationFactory
from app.calculator_memento import CalculatorMemento
from app.calculator_config import get_history_file

HISTORY_FILE = get_history_file()

class CalculatorFacade:
    def __init__(self):
        if os.path.exists(HISTORY_FILE):
            self.history = pd.read_csv(HISTORY_FILE)
            print("Previous history loaded.")
        else:
            self.history = pd.DataFrame(columns=["Operand A", "Operator", "Operand B", "Result"])

        self.undo_stack = []
        self.redo_stack = []
        self.running = True

    def save_memento(self):
        self.undo_stack.append(CalculatorMemento(self.history))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        self.redo_stack.append(CalculatorMemento(self.history))
        self.history = self.undo_stack.pop().get_state()
        print("Undo successful.")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        self.undo_stack.append(CalculatorMemento(self.history))
        self.history = self.redo_stack.pop().get_state()
        print("Redo successful.")

    def execute_command(self, command: str):
        if command in ["exit", "quit"]:
            print("Saving history...")
            self.save_history()
            print("Exiting calculator.")
            self.running = False

        elif command == "help":
            self.print_help()

        elif command == "clear":
            os.system('clear' if os.name == 'posix' else 'cls')

        elif command == "history":
            print(self.history)

        elif command == "undo":
            self.undo()

        elif command == "redo":
            self.redo()

        else:
            try:
                operator, a, b = command.split()
                a = float(a)
                b = float(b)

                self.save_memento()
                calc = CalculationFactory.create(a, b, operator)
                result = calc.perform()

                print(f"Result: {result}")
                self.history.loc[len(self.history)] = [a, operator, b, result]

            except ValueError as ve:
                print(f"Input error: {ve}")
            except Exception as e:
                print(f"Error: {e}")

    def print_help(self):
        print("Commands:")
        print("  [operator] [a] [b] → e.g., + 5 3")
        print("  Supported operators: +, -, *, /, ^, root")
        print("  history             → View calculation history")
        print("  undo                → Undo last calculation")
        print("  redo                → Redo last undone calculation")
        print("  clear               → Clear the screen")
        print("  help                → Show this help menu")
        print("  exit or quit        → Exit the calculator")

    def save_history(self):
        self.history.to_csv(HISTORY_FILE, index=False)

def repl():
    facade = CalculatorFacade()
    print("Enhanced Calculator. Type 'help' for options.\n")

    while facade.running:
        command = input(">>> ").strip().lower()
        if command:
            facade.execute_command(command)

if __name__ == "__main__":
    repl()
