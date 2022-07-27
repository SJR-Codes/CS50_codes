"""
* CS50P Problem Set 6
* CS50 P-Shirt
* by Samu Reinikainen 27.07.2022
"""

import sys
import PIL

#check that we have right amount of args
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
#check that we handle only csv files
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
