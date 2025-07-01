# Enhanced Calculator Application

## 📘 Project Description

The Enhanced Calculator is a modular, object-oriented Python command-line application that performs basic and advanced arithmetic operations. It integrates design patterns like **Factory**, **Memento**, and **Observer**, and includes features such as:

- Addition, Subtraction, Multiplication, Division, Power, and Root
- Undo/Redo support using the Memento pattern
- History logging and auto-saving with Observer pattern
- Fully tested using `pytest` with CI/CD integration via GitHub Actions
- CSV-based operation history and optional logging support

---

## ⚙️ Installation Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/jc2552-celo/enhanced-calculator.git
cd enhanced-calculator

Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Configuration Setup
Create a .env file in the project root and add the following environment variables:

ini
Copy code
CALCULATOR_MODE=cli
HISTORY_CSV=history.csv
LOG_FILE=calculator.log

Usage Guide
Run the calculator from the terminal:
python main.py

Supported Commands:
add 2 3 → Performs 2 + 3

subtract 5 2 → Performs 5 - 2

multiply 4 6 → Performs 4 × 6

divide 8 2 → Performs 8 ÷ 2

power 2 3 → Performs 2³

root 27 3 → Performs ³√27

undo → Undo the last operation

redo → Redo the last undone operation

history → Show calculation history

exit → Exit the application

🧪 Testing Instructions
Run all unit tests using pytest:

bash
Copy code
pytest -v
Check test coverage:

bash
Copy code
pytest --cov=calcapp
🔄 CI/CD Information
This project uses GitHub Actions to automate testing and validation:

Each push to main triggers a test run using pytest.

If all tests pass, the build is marked successful.

CI/CD ensures code reliability, maintainability, and deploy readiness.

✅ Latest Status: All tests passed — Commit 2793cc5

📝 Code Documentation
Every class and function includes Python docstrings.

Code is commented clearly to explain logic, especially for:

Factory pattern in calculation_factory.py

Memento logic in memento.py

Observers in observers.py

🧾 Logging & History
Logging is handled using Python’s logging module. Output includes operation details and is written to calculator.log (configured via .env).

Calculation history is automatically saved in history.csv using the AutoSaveObserver.

👤 Author
Jason Codiot
GitHub: jc2552-celo

markdown
Copy code

5. **Save the file and exit**  
- In VS Code: Just click Save.
- In Nano: Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.

6. **View your README in the terminal (optional)**

```bash
cat README.md

