"""
* CS50P Problem Set 7
* Watch on YouTube
* by Samu Reinikainen 28.07.2022
"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    p = "(src=\"\")?"
    m = re.search(p, m, re.IGNORECASE)




if __name__ == "__main__":
    main()