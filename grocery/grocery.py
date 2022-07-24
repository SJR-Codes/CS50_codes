"""
* CS50P Problem Set 3
* Grocery List
* by Samu Reinikainen 24.07.2022
"""

def main():
    slist = (get_input("Remembery to buy? "))

    print(f"Total: ${price:.2f}")

def get_input(prompt):

    while True:
        try:
            slist += input(prompt)
        except EOFError:
            return slist
