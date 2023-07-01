from plates import is_valid

def test_startchar():
    assert is_valid("CS50") == True
    assert is_valid("CSS50") == True
    assert is_valid("C4MEN") == False
    assert is_valid("2SMALL") == False
    assert is_valid("24MALL") == False
def test_first0():
    assert is_valid("CS05") == False
def test_midnum():
    assert is_valid("CS50P") == False
    assert is_valid("CS50P2") == False
def test_punc():
    assert is_valid("P13.14") == False
    assert is_valid("DE\D") == False
def test_lettercount():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


