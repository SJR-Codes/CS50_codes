"""
* CS50P Problem Set 8
* Seasons of Love
* by Samu Reinikainen 29.07.2022
"""

import sys
import re
import inflect
from datetime import date


def main():
    today = str(date.today())
    minutes = dates_to_minutes(get_bday(), today)
    print(sing_minutes(minutes))


def get_bday():
    bday = input("Your birthday (YYYY-MM-DD): ").strip()
    if re.search(r"^[\d][\d][\d][\d]-[0-1][\d]-[0-3][\d]$", bday):
        return bday
    else:
        sys.exit()

def dates_to_minutes(date_start, date_end):
    try:
        ds = date.fromisoformat(date_start)
        de = date.fromisoformat(date_end)
    except ValueError:
        sys.exit()

    diff = de - ds
    minutes = int(diff.total_seconds()/60)

    #print(f"{de} - {ds} = {minutes}")

    return minutes

def sing_minutes(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes)

    return words.capitalize() + " minutes."

if __name__ == "__main__":
    main()
