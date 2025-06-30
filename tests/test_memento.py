from calcapp.memento import Caretaker

def test_undo_redo():
    caretaker = Caretaker()
    caretaker.save_state(("add", 1, 2, 3))
    caretaker.save_state(("multiply", 2, 3, 6))

    history = caretaker.get_history()
    assert history == [
        ("add", 1, 2, 3),
        ("multiply", 2, 3, 6)
    ]

    undone = caretaker.undo()
    assert undone == ("multiply", 2, 3, 6)

    redone = caretaker.redo()
    assert redone == ("multiply", 2, 3, 6)

