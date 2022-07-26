"""
* CS50P Problem Set 5
* Test Vanity Plates
* by Samu Reinikainen 26.07.2022
"""

from plates import is_valid

def test_str_lenghth():
    assert is_valid("AAAAAA") == True
    assert is_valid("AA") == True
    assert is_valid("AAAAAAAA") == False
    assert is_valid("A") == False
