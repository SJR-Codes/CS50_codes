"""
* CS50P Problem Set 8
* Cookie Jar
* by Samu Reinikainen 30.07.2022
"""

class Jar:
    def __init__(self, capacity=12):
        if is_integer(capacity) and capacity > 0:
            self.amount = 0
            self.space = capacity
        else:
            raise ValueError

    def __str__(self):
        print("🍪" * self.amount)

    def deposit(self, n):
        if n > 0 and self.amount+n <= self.space:
            self.amount += n
        else:
            raise ValueError

    def withdraw(self, n):
        if n > 0 and self.amount-n >= 0:
            self.amount -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self.space

    @property
    def size(self):
        return self.amount

def main():
    pot = Jar()


if __name__ == "__main__":
    main()
