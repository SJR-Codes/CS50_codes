"""
* CS50P Problem Set 8
* Test Seasons of Love
* by Samu Reinikainen 29.07.2022
"""

from seasons import dates_to_minutes, sing_minutes

def test_d2m_valid():
    assert dates_to_minutes("1999-05-05", ) == "1999-05-05"


    assert dates_to_minutes("1999-05-35") == "Invalid date"
    assert dates_to_minutes("1999-05-") == "Invalid date"
    assert dates_to_minutes("aaaa-bb-cc") == "Invalid date"