# tests/test_calculator_config.py

from app import calculator_config as config

def test_config_defaults():
    assert config.HISTORY_FILE == "data/history.csv"
    assert config.LOG_FILE == "logs/app.log"
    assert config.ALLOWED_OPERATIONS == ["add", "subtract", "multiply", "divide", "power", "sqrt"]
