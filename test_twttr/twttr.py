"""
* CS50P Problem Set 2
* Just setting up my twttr
* by Samu Reinikainen 23.07.2022
"""

def main():
    uinp = input("Say what? ")

    print(shorten(uinp))


def shorten(uinp):
    #remove vowels (A, E, I, O, and U)
    rem_vowls = ["A","E","I","O","U"]
    ret = ""

    for x in uinp:
        #if x.upper() not in rem_vowls:
        if x not in rem_vowls:
            ret += x

    return ret

if __name__ == "__main__":
    main()