"""
* CS50P Problem Set 3
* Outdated
* by Samu Reinikainen 24.07.2022
"""

def main():
    print("What date is it (\"(m/d/y)\")? ")
    odate = get_input("")

    #slist.sort()

    print_list(slist)

def get_input(prompt):
    x = []
    while True:
        try:
            input(prompt)
        except EOFError:
            return slist


main()