"""
* CS50P Problem Set 1
* Math Interpreter
* by Samu Reinikainen 22.07.2022
"""

def main():
    #operands
    ops = ["+", "-", "*", "/"]

    uinp = input("Enter your homework: ").split(" ")
    print(uinp)
    if uinp[0].isnumeric() and uinp[2].isnumeric() and uinp[1] in ops:
        #x = int(uinp[0])
        #y = int(uinp[2])
        x = uinp[0]
        y = uinp[2]
        op = uinp[1]
        print(x + op + y)
        if op == "/" and y == 0:
            print("Can't compute!!!")
        else:
            res = float(eval(x + op + y), 1)
            print(res)
    else:
        print("Can't compute!!!")




main()