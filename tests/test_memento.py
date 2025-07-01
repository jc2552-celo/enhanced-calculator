from calcapp.memento import Caretaker

def test_undo_redo():
    caretaker = Caretaker()
    caretaker.save("add", 1, 2, 3)
    caretaker.save("multiply", 2, 3, 6)
    
    undone = caretaker.undo()
    assert undone == ("multiply", 2, 3, 6)

    redone = caretaker.redo()
    assert redone == ("multiply", 2, 3, 6)

