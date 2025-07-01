from calcapp.observers import LoggingObserver, AutoSaveObserver
import logging

def test_logging_observer(tmp_path):
    log_file = tmp_path / "test_log.txt"
    observer = LoggingObserver()

    handler = logging.FileHandler(log_file)
    observer_logger = logging.getLogger("calcapp")
    observer_logger.setLevel(logging.INFO)
    observer_logger.addHandler(handler)

    observer.update("add", 2, 3, 5)

    with open(log_file, 'r') as f:
        contents = f.read()
    assert "Operation performed: add 2 3 = 5" in contents

