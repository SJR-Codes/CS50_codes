"""
* CS50P Problem Set 8
* Test Cookie Jar
* by Samu Reinikainen 30.07.2022
"""

import pytest
import jar

def test_init():
    with pytest.raises(ValueError):
        pot = jar.Jar(-1)
    with pytest.raises(ValueError):
        pot = jar.Jar("gaa")

def test_deposit():
    pot = jar.Jar(5)
    with pytest.raises(ValueError):
        pot.deposit(-5)
    with pytest.raises(ValueError):
        pot.deposit("10")
    with pytest.raises(ValueError):
        pot.deposit("guu")

def test_withdraw():
    pot = jar.Jar(3)
    with pytest.raises(ValueError):
        pot.withdraw(-5)
    with pytest.raises(ValueError):
        pot.withdraw("10")
    with pytest.raises(ValueError):
        pot.withdraw("guu")