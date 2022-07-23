"""
* CS50P Problem Set 2
* Coke Machine
* by Samu Reinikainen 23.07.2022
"""

def main():
    coke_price = 50
    accept_change = [25, 10, 5]
    amount = 0

    while amount < coke_price:
        change = int(input("Enter money(25c, 10c or 5c): "))
        if change in accept_change:
            amount += change
        print("Amount due: " + str(coke_price - amount))





main()