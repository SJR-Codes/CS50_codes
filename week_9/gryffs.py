"""
* CS50P Problem Set 8
* Notes week 9: conditional list comprehension, filter
* by Samu Reinikainen 30.07.2022
"""


students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]
"""
gryffs = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryff in sorted(gryffs):
    print(gryff)
"""

def is_gryff(s):
    return s["house"] == "Gryffindor"

gryffs = filter(is_gryffindor, students)

for gryff in sorted(gryffs):
    print(gryff)