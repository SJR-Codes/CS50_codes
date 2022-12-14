"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

import re

name = input("Give me your name: ").strip()

#David Malan or Malan, David
"""
if ", " in name:
    lname, fname = name.split(", ")
    name = f"{fname} {lname}"
"""

##matches = re.search("^(\w+), *(\w+)$", name)
##if matches:
# or one-liner with walrus-operator :=
if matches := re.search("^(\w+), *(\w+)$", name):
    #lname, fname = matches.groups()
    lname = matches.group(1)
    fname = matches.group(2)
    print(matches)
    name = f"{fname} {lname}"

print(f"Hello, {name}")