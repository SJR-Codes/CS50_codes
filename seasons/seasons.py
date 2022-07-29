"""
* CS50P Problem Set 8
* Seasons of Love
* by Samu Reinikainen 29.07.2022
"""

import sys
import re
from datetime import date


def main():
    minutes = dates_to_minutes(get_bday(), date.today())
    print(minutes)


def get_bday():
    #bday = input("Your birthday (YYYY-MM-DD): ").strip()
    bday = "1999-05-05"
    #bday = "1999-05-"
    if re.search("^[\d][\d][\d][\d]-[0-1][\d]-[0-3][\d]$", bday):
        return bday
    else:
        sys.exit("Invalid date")

def dates_to_minutes(date_start, date_end):
    ds = date.fromisoformat(date_start)
    de = date_end


if __name__ == "__main__":
    main()
