"""
* CS50P Problem Set 7
* Test Working 9 to 5
* by Samu Reinikainen 28.07.2022
"""

from working import convert

def test_valid():
    assert convert("09:00 AM to 05:00 PM") == ""


def test_invalid():
    assert convert() == ""