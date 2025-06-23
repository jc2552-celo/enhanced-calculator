from app.calculation_factory import CalculationFactory
from app.history import CalculationHistory
from app.observers import LoggerObserver

def repl():
    history = CalculationHistory()
    logger = LoggerObserver()

    print("Welcome to the Enhanced Calculator!")
    print("Available operations: add, subtract, multiply, divide, power, root")
    print("Type 'history' to view past results, or 'exit' to quit.\n")

    while True:
        operation = input("Enter operation: ").strip().lower()

        if operation == "exit":
            break
        elif operation == "history":
            for item in history.get_history():
                print(item)
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            calculation = CalculationFactory.create(operation, a, b)
            calculation.attach(logger)
            result = calculation.execute()
            print("Result:", result)
            history.add_calculation(calculation)

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except KeyError:
            print(f"Invalid operation '{operation}'. Try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

