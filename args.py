"""
* CS50P Problem Set 8
* Notes week 9: using command line arguments
* by Samu Reinikainen 30.07.2022
"""

import sys


if len(sys.argv) == 1:
    print("miau")
else:
    print("Usage: args.py -n 3")