"""
* CS50P Problem Set 8
* Notes week 9: Type Hints
* by Samu Reinikainen 30.07.2022
"""

#pip install mypy
#use: mypy type_hints.py to error check


MIAUS = 3
"""
#type hint n as int "n: int"
#python itself does not care about type hints but they help error checking with ie. mypy

def miau(n: int):
    for _ in range(n):
        print("Miau!")

#type hints can be used outside of function arguments
numb: int = int(input("Number: "))
miau(numb)

"""

#type hinting functions return value
def miau(n: int) -> None:
    for _ in range(n):
        print("Miau!")

#type hints can be used outside of function arguments
numb: int = int(input("Number: "))
miaus: str = miau(numb)

print(miaus)