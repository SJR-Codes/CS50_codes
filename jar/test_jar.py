"""
* CS50P Problem Set 8
* Test Cookie Jar
* by Samu Reinikainen 30.07.2022
"""

import pytest
import jar

def test_init():
     with pytest.raises(ValueError):
        jar = Jar()