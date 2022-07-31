"""
* CS50P Problem Set 9
* Notes week 9: conditional list comprehension, filter
* by Samu Reinikainen 31.07.2022
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

gryffs = filter(is_gryff, students)

#sorting dictionary with lambda keys
for gryff in sorted(gryffs, key=lambda s: s["name"]):
    print(gryff["name"])


students = ["Hermione","Harry","Ron"]

"""
gryffs = []

for student in students:
    gryffs.append({"name": student, "house": "Gryffindor"})
"""

#gryffs = [{"name": student, "house": "Gryffindor"} for student in students]

#dictionary comprehension

gryffs = {student: "Gryffindor" for student in students}


print(gryffs)