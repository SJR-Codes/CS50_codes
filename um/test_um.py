"""
* CS50P Problem Set 7
* Test Working 9 to 5
* by Samu Reinikainen 28.07.2022
"""

import pytest
from um import count

def test_simple():
    assert count("Regular, um, Expressions") == 1
    assert count("Regular, um, um, Expressions") == 2


def test_um_in():
    assert count("Regular yummy Expressions") == 0
    assert count("Regular mum Expressions") == 0
    assert count("Regular, um, mum, Expressions") == 1

def test_garble():
    assert count(" ") == 0
    assert count("1234um435") == 0
    assert count("1234 um, 435") == 1