"""
* CS50P Problem Set 2
* Nutrition Facts
* by Samu Reinikainen 23.07.2022
"""

def main():
    x = (get_input("Enter fraction (x/y, ie. 3/4): "))


def get_input(prompt):
    while True:
        x = input(prompt)

def check_input(x):

        if(x.count("/") == 1):
            return x.split("/")


def fract_to_gauge(fract):
    #convert fract to gauge, ie. 3/4 = 75%
    pass



main()