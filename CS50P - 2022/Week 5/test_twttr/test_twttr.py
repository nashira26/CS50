from twttr import shorten

def test_low():
    assert shorten("twitter") == "twttr"
def test_up():
    assert shorten("TWITTER") == "TWTTR"
def test_num():
    assert shorten("twitter456") == "twttr456"
def test_punc():
    assert shorten("twitter!") == "twttr!"