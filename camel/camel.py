"""
* CS50P Problem Set 1
* Camel Case
* by Samu Reinikainen 23.07.2022
"""

def main():
    varname = input("Enter variable name: ")

    print(snakify(varname))


def snakify(vname):
    #convert string from camel case to snake case
    ret = ""
    while char in vname:
        if isupper(char):
            ret = ret + "_" + lower(char)
        else:
            ret = ret + char

    return ret

main()