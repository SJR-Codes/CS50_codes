"""
* CS50P Problem Set 6
* CS50 P-Shirt
* by Samu Reinikainen 27.07.2022
"""

import sys
from PIL import Image

#check that we have right amount of args
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

#check that we handle only "jpg", "jpeg","png" files
valid_exts = ["jpg", "jpeg","png"]
intmp = sys.argv[1].lower().rsplit(".")
if intmp[1] not in valid_exts:
    sys.exit("Invalid file format")

outtmp = sys.argv[2].lower().rsplit(".")
if outtmp[1] not in valid_exts:
    sys.exit("Invalid output")

if intmp != outtmp:
    sys.exit("Input and output have different extensions")

try:
    image = Image.open(arg)
except FileNotFoundError:
    sys.exit("Input does not exist")

