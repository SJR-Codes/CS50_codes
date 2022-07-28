"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

import re

twit = "Hei https://twitter.com/huuhaauser" #input("Give me your twitter: ").strip()


#uname = twit.replace("https://twitter.com/", "")
uname = twit.removeprefix("https://twitter.com/")

# if uname := re.search("")


print(f"Username: {uname}")