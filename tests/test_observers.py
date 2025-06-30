import pandas as pd
from calcapp.observers import LoggingObserver, AutoSaveObserver
from pathlib import Path


def test_logging_observer(tmp_path):
    log_file = tmp_path / "test_log.txt"
    observer = LoggingObserver()
    
    # Patch logger to write to file for testing
    import logging
    handler = logging.FileHandler(log_file)
    observer_logger = logging.getLogger("calcapp")
    observer_logger.setLevel(logging.INFO)
    observer_logger.addHandler(handler)

    observer.update(("add", 2, 3, 5))

    observer_logger.removeHandler(handler)
    handler.close()

    with open(log_file, "r") as file:
        logs = file.read()
        assert "Performed add with 2 and 3 = 5" in logs


def test_auto_save_observer(tmp_path):
    csv_file = tmp_path / "test_history.csv"
    observer = AutoSaveObserver(str(csv_file))
    observer.update(("multiply", 4, 2, 8))

    df = pd.read_csv(csv_file)
    assert df.iloc[0].to_dict() == {
        "operation": "multiply",
        "a": 4,
        "b": 2,
        "result": 8
    }

