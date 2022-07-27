"""
* CS50P Problem Set 6
* Notes for week 6
* by Samu Reinikainen 27.07.2022
"""

import csv

students = []

with open("names.csv") as file:
    reader = csv.reader(file)
    for name, foo in reader:
        students.append({"name": name, "foo": foo})

for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name'].title()} from {student['foo']}")
