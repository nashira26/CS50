from um import count
import pytest

def test_wordalone():
    assert count("um") == 1
    assert count("Hello, um, world") == 1
    assert count("This is um.. CS50") == 1
    assert count("Um.. how are you?") == 1
    assert count("Um.. thanks, um, makes sense") == 2
    assert count("Um? Mum? that album where, um, umm, that album?") == 2

def test_wordspaced():
    assert count("hi Um who are you") == 1

def test_inwords():
    assert count("hi Um this is yummy") == 1
    assert count("hi yummy") == 0

def test_casesens():
    assert count("Um.. thanks, um, makes sense") == 2