from bank import value

def test_100():
    assert value("  Hello") == 100
    assert value("Yello") == 100

def test_20():
    assert value("Hi") == 20
    assert value("How are you") == 20

def test_0():
    assert value("Hello") == 0
    assert value("Hello, sir") == 0

