"""
* CS50P Problem Set 8
* Notes week 9: Docstrings
* by Samu Reinikainen 30.07.2022
"""

#document functions with docstrings for creating documentation ie. with sphinx

# Uses Sphinx docstring format


def miau(n: int) -> str:
    """
    Returns string "Miau! " n number of times.

    :param n: Number of times to Miau
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n Miaus! on one line
    :rtype: str
    """
    return "Miau! " * n

numb: int = int(input("Number: "))
miaus: str = miau(numb)

print(miaus)