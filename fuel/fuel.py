"""
* CS50P Problem Set 2
* Nutrition Facts
* by Samu Reinikainen 23.07.2022
"""

def main():
    x = (get_input("Enter fraction (x/y, ie. 3/4): "))
    #print(x)

def get_input(prompt):
    while True:
        x = check_input(input(prompt))
        #print(x)
        if x != False:
            return x

def check_input(fract):
    if(fract.count("/") == 1):
        fract = fract.split("/")
    else:
        return False

    try:
        x = int(fract[0])
        y = int(fract[1])
    except ValueError:
        print("Value Error: Not valid fraction!")
        return False

    if y <= 0 or x < 0:
        print("Zero or Negative Number Error: Not valid fraction!")
        return False

    return fract


def fract_to_gauge(fract):
    #convert fract to gauge, ie. 3/4 = 75%
    pass



main()