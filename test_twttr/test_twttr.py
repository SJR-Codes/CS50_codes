from twttr import shorten

def test_words():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Tweet") == "Twt"

def test_words_with_y():
    assert shorten("Titty") == "Ttty"
    assert shorten("Tweety") == "Twty"

def test_words_upper():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Tweet") == "Twt"