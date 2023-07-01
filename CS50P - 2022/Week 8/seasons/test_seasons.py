from seasons import validate, age

def test_validate():
    assert validate("1996-05-27") == 1996-05-27
    assert validate("1996-02-28") == 1996-02-28
    with pytest.raises(ValueError):
        validate("1996-02-30")
        validate("1996-17-15")
        validate("1996.12.15")
        validate("1996-9-7")
        validate("15-12-1996")
        validate("November 1, 1996")

def test_age():
    age("1996-12-15") = 13752000
