from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(2)
    assert jar1.capacity == 2
    with pytest.raises(ValueError):
        jar2 = Jar(-2)
        jar3 = Jar("two")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(6)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(4)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(3)