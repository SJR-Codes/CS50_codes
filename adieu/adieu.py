"""
* CS50P Problem Set 4
* Adieu, Adieu
* by Samu Reinikainen 25.07.2022
"""

def main():
    #slist = sort_list(get_input("Remember to buy? "))
    slist = sort_list(get_input(""))

    #slist.sort()

    print_list(slist)

def get_input(prompt):
    slist = []
    while True:
        try:
            slist.append(input(prompt).upper())
        except EOFError:
            return slist

