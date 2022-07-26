"""
* CS50P Problem Set 5
* Just testing my twttr
* by Samu Reinikainen 26.07.2022
"""

def main():
    uinp = input("Say what? ")

    print(shorten(uinp))


def shorten(uinp):
    #remove vowels (A, E, I, O, and U)
    rem_vowls = ["A","E","I","O","U"]
    ret = ""

    try:
        str(uinp)
    except TypeError:
        return ret

    for x in uinp:
        if x.upper() not in rem_vowls:
            ret += x

    return ret

if __name__ == "__main__":
    main()