"""
* CS50P Problem Set 7
* Working 9 to 5
* by Samu Reinikainen 28.07.2022
"""

import re
import sys

def main():
    #print(convert(input("Hours: ")))
    convert("09:00 AM to 05:00 PM")


def convert(s):
    #09:00 AM to 05:00 PM
    p = "^([0-1]?[0-9]:?(?:[0-5][0-6])?.[AM|PM]) to ([0-1]?[0-9]:?(?:[0-5][0-6])?.[AM|PM])$"
    try:
        if m := re.search(p, s, re.IGNORECASE):
            print(m.group(1))
            print(m.group(2))
        else:
            raise ValueError
    except ValueError:
        pass
    #    sys.exit()





if __name__ == "__main__":
    main()