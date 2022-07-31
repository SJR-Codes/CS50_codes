"""
* CS50P Problem Set 8
* Notes week 9: Globals
* by Samu Reinikainen 30.07.2022
"""

balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    print("Balance:", balance)
    deposit(50)
    print("Balance:", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()
