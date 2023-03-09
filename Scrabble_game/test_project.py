import pytest
from project import valid, compute_score, winner

def test_valid():
    assert valid("cat") == True
    assert valid("hammer") == True
    assert valid("gh") == False
    assert valid("jkl") == False

def test_compute_score():
    assert compute_score("cat") == 5
    with pytest.raises(NameError):
        compute_score("fj")
    with pytest.raises(ValueError):
        compute_score("123")

def test_winner():
    assert winner({'a': 14, 'd': 18, 'c': 10}) == "The winner is d!"
    assert winner({'1': 89, 'he': 60, '5f': 100}) == "The winner is 5f!"
    assert winner({'a': 14, 'd': 10, 'c': 14}) == "It's a tie. The winners are a, c!!"
