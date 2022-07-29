"""
* CS50P Problem Set 8
* Test Seasons of Love
* by Samu Reinikainen 29.07.2022
"""

from pytest import 
from seasons import dates_to_minutes, sing_minutes

def test_d2m_valid():
    assert dates_to_minutes("2021-07-29", "2022-07-29") == 525600
    assert dates_to_minutes("2020-07-29", "2022-07-29") == 1051200

def test_d2m_invalid():
    assert dates_to_minutes("1999-05-35", "2022-07-29") == ""
    assert dates_to_minutes("1999-05-", "2022-07-29") == ""
    assert dates_to_minutes("aaaa-bb-cc", "2022-07-29") == ""