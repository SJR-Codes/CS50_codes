"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

import re

twit = "Hei https://twitter.com/huuhaauser/?foo=bar" #input("Give me your twitter: ").strip()


#uname = twit.replace("https://twitter.com/", "")
uname = twit.removeprefix("https://twitter.com/")

# if uname := re.search("")
#re.sub(pattern, replace, twit)
#uname = re.sub(".*(http|https)://twitter\.com/", "", twit)
#uname = re.sub(".*(https?://)?(www\.)?twitter\.com/", "", twit)
#uname = re.sub("\w*/", "", twit)
#uname := re.sub(".*(https?://)?(www\.)?twitter\.com/", "", twit):

pattern = ".*(?:https?://)?(?:www\.)?twitter\.com/(\w+)"
if uname := re.search(pattern, twit, re.IGNORECASE):
    print(f"Username: {uname.group(1)}")
else:
    print(f"{twit} is not valid!")