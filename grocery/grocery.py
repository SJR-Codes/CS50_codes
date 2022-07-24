"""
* CS50P Problem Set 3
* Grocery List
* by Samu Reinikainen 24.07.2022
"""

def main():
    slist = sort_list(get_input("Remember to buy? ")))

    #slist.sort()

    print(slist)

def get_input(prompt):
    slist = []
    while True:
        try:
            slist.append(input(prompt).upper())
        except EOFError:
            return slist

def sort_list(slist):
    final_list = {}

    slist.sort()

    for item in slist:
        x = final_list.get(item, 0)
        if x == 0:
            final_list[item] = 1
        else:
            final_list[item] += 1


main()