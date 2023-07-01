from bank import value

def test_0():
    assert value("hello") == 0
def test_20():
    assert value("hey") == 20
def test_100():
    assert value("are you fine?") == 100
def test_cap20():
    assert value("Hey") == 20
def test_20():
    assert value("hey") == 20
