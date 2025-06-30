# tests/test_history.py

import os
import pandas as pd
from app.history import CalculationHistory

def test_add_entry_and_history(tmp_path):
    file_path = tmp_path / "history.csv"
    history = HistoryManager(str(file_path))

    history.add_entry("add", 2, 3, 5)
    assert not history.df.empty
    assert history.df.iloc[-1]["result"] == 5

def test_save_and_load_history(tmp_path):
    file_path = tmp_path / "history.csv"
    history = HistoryManager(str(file_path))
    history.add_entry("multiply", 4, 5, 20)
    history.save_history()

    new_history = HistoryManager(str(file_path))
    assert len(new_history.df) == 1
    assert new_history.df.iloc[0]["result"] == 20

def test_undo_redo(tmp_path):
    file_path = tmp_path / "history.csv"
    history = HistoryManager(str(file_path))

    history.add_entry("subtract", 10, 2, 8)
    assert len(history.df) == 1

    undo_result = history.undo()
    assert undo_result == "Last operation undone."
    assert history.df.empty

    redo_result = history.redo()
    assert redo_result == "Redo completed."
    assert len(history.df) == 1

def test_clear(tmp_path):
    file_path = tmp_path / "history.csv"
    history = HistoryManager(str(file_path))

    history.add_entry("power", 2, 3, 8)
    history.clear()
    assert history.df.empty
