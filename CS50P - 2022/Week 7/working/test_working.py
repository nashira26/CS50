from working import convert
import pytest

def test_firsttype():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9 AM to 12:14 PM") == "09:00 to 12:14"
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
        convert("9AM - 5PM")
        convert("13 AM to 5 PM")
        convert("4 AM 5:12 PM")

def test_secondtype():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9:05 AM to 5:00 PM") == "09:05 to 17:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:00 PM")
        convert("09:00 to 17:00")
        convert("10:7 AM to 5:1 PM")
        convert("10:00 AM 5:00 PM")
        convert("9:00 AM to 17:00 PM")

def test_omitto():
    assert convert("10:00 AM to 5:00 PM") == "10:00 to 17:00"
    assert convert("4 AM to 5:12 PM") == "04:00 to 17:12"
    with pytest.raises(ValueError):
        convert("10:00 AM 5:00 PM")
        convert("4 AM 5:12 PM")

def test_outofrange():
    assert convert("8:59 AM to 4:00 PM") == "08:59 to 16:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
     with pytest.raises(ValueError):
        convert("8:60 AM to 4:00 PM")
        convert("09:00 to 17:00")
        convert("23:00 to 90:00")





