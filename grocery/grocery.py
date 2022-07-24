"""
* CS50P Problem Set 3
* Grocery List
* by Samu Reinikainen 24.07.2022
"""

def main():
    price = (get_input("What's your pleasure, sir? "))

    print(f"Total: ${price:.2f}")

def get_input(prompt):
    price = 0
    while True:
        try:
            price += get_price(input(prompt))
            print(f"Total: ${price:.2f}", end=" ")
        except EOFError:
            return price
