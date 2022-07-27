"""
* CS50P Problem Set 6
* Scourgify
* by Samu Reinikainen 27.07.2022
"""

import sys
import csv

#check that we have right amount of args
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
#check that we handle only csv files
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

lines = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

for line in lines[1:]:
    print(line)
    tmp = line
