"""
* CS50P Problem Set 7
* Test Response
* by Samu Reinikainen 28.07.2022
"""

import pytest
from response import check

def test_valid():
    assert check("ad@ad.fi") == "Valid"
    assert check("asd@sub.ad.edu") == "Valid"
    assert check("foo.bar@test.edu") == "Valid"

def test_invalid():
    assert check("ad@adfi") == "Invalid"
    assert check("asd@sub.ad.") == "Invalid"
    assert check("foo.bar@") == "Invalid"

def test_garble():
    assert check(" ") == "Invalid"
