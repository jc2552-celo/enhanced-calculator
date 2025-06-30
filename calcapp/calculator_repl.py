from calcapp.calculation_factory import CalculationFactory
from calcapp.exceptions import OperationError
from calcapp.observers import LoggingObserver, AutoSaveObserver
from calcapp.memento import Caretaker

def repl():
    print("Welcome to the Enhanced Calculator! Type 'help' for commands.")
    history = []
    caretaker = Caretaker()

    observer1 = LoggingObserver("logs/calc.log")
    observer2 = AutoSaveObserver("history/history.csv")
    observers = [observer1, observer2]

    while True:
        user_input = input(">> ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "help":
            print("Commands: add, subtract, multiply, divide, history, undo, redo, exit")
        elif user_input == "history":
            for i, (op, a, b, result) in enumerate(history, 1):
                print(f"{i}: {op} {a} {b} = {result}")
        elif user_input == "undo":
            history = caretaker.undo(history)
            print("Last operation undone.")
        elif user_input == "redo":
            history = caretaker.redo(history)
            print("Redo performed.")
        else:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Example: add 4 5")
                continue

            op, a_str, b_str = parts
            try:
                a = float(a_str)
                b = float(b_str)
                operation = CalculationFactory.create(op, a, b)
                result = operation.execute()
                print(f"Result: {result}")
                history.append((op, a, b, result))
                caretaker.save(history)
                for obs in observers:
                    obs.update(op, a, b, result)
            except (ValueError, OperationError) as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    repl()

