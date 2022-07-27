"""
* CS50P Problem Set 6
* Lines of Code
* by Samu Reinikainen 27.07.2022
"""

import sys

try:
    f = open(sys.argv[1], "r")
except IndexError:
    sys.exit("Enter filename.")
except IndexError:
    sys.exit("Enter filename.")

