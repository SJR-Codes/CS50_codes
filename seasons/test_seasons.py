"""
* CS50P Problem Set 8
* Test Seasons of Love
* by Samu Reinikainen 29.07.2022
"""

from seasons import get_bday

def test_bday():
    assert get_bday("1999-05-05") == "1999-05-05"
    assert get_bday("1999-05-35") == "Invalid date"
    assert get_bday("1999-05-") == "Invalid date"
    assert get_bday("aaaa-bb-cc") == "Invalid date"