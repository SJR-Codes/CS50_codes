"""
* CS50P Problem Set 4
* Little Professor
* by Samu Reinikainen 25.07.2022
"""

import sys
import random

def main():
    #print("Level: ", end="")
    level = get_level("Level: ")

    sys.exit("6 + 6 = ")

def get_level(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue

if __name__ == "__main__":
    main()