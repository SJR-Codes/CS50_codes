"""
* CS50P Problem Set 2
* Nutrition Facts
* by Samu Reinikainen 23.07.2022
"""

def main():
    get_input("Enter fraction (x/y, ie. 3/4): ")


def get_input(prompt):
    while True:
        try:
            x = input(prompt).split("/")
        except:
            pass



def fract_to_gauge(fract):
    #convert fract to gauge, ie. 3/4 = 75%
    pass



main()