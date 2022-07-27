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
except FileError:
    sys.exit("Enter filename.")

lcount = 0

for line in f:
    if line.strip() != "" or line.strip()[0] != "#":
        lcount += 1

print