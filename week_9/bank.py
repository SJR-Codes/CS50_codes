"""
* CS50P Problem Set 8
* Notes week 9: Globals
* by Samu Reinikainen 30.07.2022
"""

#set variable to global
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    print("Balance:", balance)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()
