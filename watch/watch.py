"""
* CS50P Problem Set 7
* Watch on YouTube
* by Samu Reinikainen 28.07.2022
"""

import re
import sys


def main():
    #print(parse(input("HTML: ")))
    url = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0" src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    print(parse(url))


def parse(s):
    p = "src=\"https?://(?:www\.)?youtube\.com/embed/(.*)\""
    if m := re.search(p, s, re.IGNORECASE):
        if len(m.groups()) == 1:
            return "https://youtu.be/" + m.group(1)

    #print(m.group(1))


if __name__ == "__main__":
    main()