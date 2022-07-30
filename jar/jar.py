"""
* CS50P Problem Set 8
* Cookie Jar
* by Samu Reinikainen 30.07.2022
"""

class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self.amount = 0
            self.capacity = 0
        else:
            raise ValueError

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...


def main():
    ...


if __name__ == "__main__":
    main()
