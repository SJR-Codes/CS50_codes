"""
* CS50P Problem Set 6
* Lines of Code
* by Samu Reinikainen 27.07.2022
"""

import sys

#check that we have right amount of args
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
#check that we handle only python files
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")


try:
    f = open(sys.argv[1], "r")
except FileError:
    sys.exit("File does not exist")

lcount = 0

for line in f:
    if line.strip() != "" or line.strip()[0] != "#":
        lcount += 1

print(lcount)