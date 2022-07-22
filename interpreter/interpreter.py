"""
* CS50P Problem Set 1
* Math Interpreter
* by Samu Reinikainen 22.07.2022
"""

main():
    #operands
    ops = ["+", "-", "*", "/"]
    uinp = input("Enter your homework: ").split(" ")

    if uinp[0].isnumeric() and uinp[2].isnumeric() and uinp[1] in ops:
        x = int(uinp[0])
        y = int(uinp[2])
        op = uinp[1]

        if op = "/" and y == 0:
            print("Can't compute!!!")
        else
            print(eval(x + op + y))
    else:
        print("Can't compute!!!")




main()