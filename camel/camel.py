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
    while x in vname:
        if isupper(x):
            ret = ret + "_" + lower(x)
        else:
            ret = ret + x

    return ret

main()