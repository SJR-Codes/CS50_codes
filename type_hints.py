"""
* CS50P Problem Set 8
* Notes week 9: Type Hints
* by Samu Reinikainen 30.07.2022
"""

#pip install mypy



MIAUS = 3

def miau(n):
    for _ in range(n):
        print("Miau!")

numb = input("Number: ")
miau(numb)