"""
* CS50P Problem Set 8
* Shitificate
* by Samu Reinikainen 30.07.2022
"""

from fpdf import FPDF

class shirt(FPDF):
    def __init__(self, name):
        if is_integer(capacity) and int(capacity) > 0:
            self.amount = 0
            self.space = int(capacity)
        else:
            raise ValueError