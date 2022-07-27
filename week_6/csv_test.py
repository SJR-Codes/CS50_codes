"""
* CS50P Problem Set 6
* Notes for week 6
* by Samu Reinikainen 27.07.2022
"""

import csv

name = input("Give name: ")
foo = input("Foo bar: ")

with open("names.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, foo])


students = []

#basic csv
"""
with open("names.csv") as file:
    reader = csv.reader(file)
    for name, foo in reader:
        students.append({"name": name, "foo": foo})
"""

#dictionary reader
with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "foo": row["foo"]})


for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name'].title()} from {student['foo']}")
