"""
* CS50P Problem Set 6
* Lines of Code
* by Samu Reinikainen 27.07.2022
"""

import sys
import tabulate
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
    with open("names.csv") as file:
        reader = csv.DictReader(file)
        headers = list(reader.keys())
        for row in reader:
            #students.append({"name": row["name"], "foo": row["foo"]})
            pizzas.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizzas, headers, tablefmt="grid"))