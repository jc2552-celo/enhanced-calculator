import logging
import csv

class LoggingObserver:
    def update(self, operation, a, b, result):
        logger = logging.getLogger("calcapp")
        logger.info(f"Operation performed: {operation} {a} {b} = {result}")


class AutoSaveObserver:
    def __init__(self, filename):
        self.filename = filename

    def update(self, operation, a, b, result):
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([operation, a, b, result])

