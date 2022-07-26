"""
* CS50P Problem Set 5
* Test Fuel Gauge
* by Samu Reinikainen 26.07.2022
"""

import fuel

def test_convert():
    assert fuel.convert("1/1") == 100

def test_gauge():
    assert fuel.gauge(100) == "F"