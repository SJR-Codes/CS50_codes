"""
* CS50P Problem Set 8
* Notes week 9: Globals
* by Samu Reinikainen 30.07.2022
"""

"""
#set variable to global
balance = 0

def main():
    #you can print global variable without declaring it global
    print("Balance:", balance)
    deposit(100)
    print("Balance:", balance)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    #to change global variable declare it global
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n
"""

class Account():
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    acc = Account()
    print("Balance:", acc.balance)
    acc.deposit(100)
    print("Balance:", acc.balance)
    acc.withdraw(50)
    print("Balance:", acc.balance)

if __name__ == "__main__":
    main()
