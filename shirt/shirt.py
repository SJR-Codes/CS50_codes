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

#check that we handle only "jpg", "jpeg","png" files
valid_exts = ["jpg", "jpeg","png"]
tmp = sys.argv[1].lower().rsplit()

    sys.exit("Not a CSV file")
