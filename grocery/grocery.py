"""
* CS50P Problem Set 3
* Grocery List
* by Samu Reinikainen 24.07.2022
"""

def main():
    slist = (get_input("Remember to buy? "))

    slist.sort()

    print(slist)

def get_input(prompt):
    slist = []
    while True:
        try:
            slist.append(input(prompt).upper())
        except EOFError:
            return slist

main()