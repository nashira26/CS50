from numb3rs import validate

def test_reg():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
def test_range():
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False
    assert validate("256.256.256.256") == False
    assert validate("cat") == False
    assert validate("255.255.255") == False
    assert validate("8.8.8") == False
    assert validate("8") == False
    assert validate("10.10.10.10.10") == False
    assert validate("2001.odb8.435v.423gr.04556") == False
