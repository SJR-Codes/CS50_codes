"""
* CS50P Problem Set 5
* Test Fuel Gauge
* by Samu Reinikainen 26.07.2022
"""

import fuel
import pytest

def test_convert():
    assert fuel.convert("1/1") == 100
    assert fuel.convert("1/2") == 50
    assert fuel.convert("0/2") == 0
    assert fuel.convert("2/0") == 0

def test_gauge():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(50) == "50%"

def test_zero_division():
    