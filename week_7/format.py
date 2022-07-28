"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

import re

name = input("Give me your name: ").strip()

#David Malan or Malan, David

if ", " in name:
    lname, fname = name.split(", ")
    name = f"{fname} {lname}"

print(f"Hello, {name}")