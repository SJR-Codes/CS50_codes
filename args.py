"""
* CS50P Problem Set 8
* Notes week 9: using named command line arguments
* by Samu Reinikainen 30.07.2022
"""

import sys


if len(sys.argv) == 1:
    print("miau")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("Miau!")
else:
    print("Usage: args.py -n 3")