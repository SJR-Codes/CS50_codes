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
    #p = "^([0-1]?[0-9]:?(?:[0-5][0-6])?.[AM|PM]) to ([0-1]?[0-9]:?(?:[0-5][0-6])?.[AM|PM])$"
    #p = "^([0-9][0-9]:?[0-9][0-9].[AM|PM]) to ([0-9][0-9]:?[0-9][0-9].[AM|PM])$"
    p = r"^([0-1]?[0-9](?::[0-5][0-9])? [A|P]M) to ([0-1]?[0-9](?::[0-5][0-9])? [A|P]M)$"
    #try:
    if m := re.search(p, s, re.IGNORECASE):
        start = convert_time(m.group(1))
        end = convert_time(m.group(2))

        return start + " to " + end
    else:
        raise ValueError
    #except ValueError:
    #    pass
    #    sys.exit()

#converts 05:00 PM or 5 PM to 17:00
def convert_time(t):
    if ":" in t:
        hour, min = split(":", t[:-3])
    else:
        hour = t[:-3]
        min = "00"
    if "PM" in t:
        int(hour) += 12

    return f"{hour}:{min}"


if __name__ == "__main__":
    main()