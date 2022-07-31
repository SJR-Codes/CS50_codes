"""
* CS50P Problem Set 8
* week 9 notes
* by Samu Reinikainen 31.07.2022
"""

#datatype: set

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

"""
houses = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print house
"""

#easier with sets
houses = set()

for student in students:
        houses.add(student["house"])

for house in sorted(houses):
    print(house)