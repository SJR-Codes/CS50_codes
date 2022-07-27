"""
* CS50P Problem Set 6
* Lines of Code
* by Samu Reinikainen 27.07.2022
"""

import sys
from tabulate import tabulate
import csv

#check that we have right amount of args
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
#check that we handle only csv files
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

pizzas = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            #headers = list(row.keys())
            pizzas.append(row)
            #print(row)
except FileNotFoundError:
    sys.exit("File does not exist")

headers = list(pizzas[0].keys())

#tmp = headers + pizzas

print(headers)

#print(reader)
#print(tabulate(tmp, headers="firstrow", tablefmt="grid"))