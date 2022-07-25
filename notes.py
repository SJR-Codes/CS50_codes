"""
* CS50P Problem Set 4
* Notes
* by Samu Reinikainen 25.07.2022
"""
#import random
#flip = random.choice(["kruuna","klaava"])

#or explicitly just one functions
"""
from random import choice
flip = choice(["kruuna","klaava"])

print(flip)
"""

import random as r
"""
number = r.randint(1,10)

print(number)

cards = ["Jack", "Queen", "King", "Ace"]
#print(cards)
r.shuffle(cards)
for card in cards:
    print(card)

import statistics as s

print(s.mean([100,90,90]))
"""
import sys
"""
try:
    print("Hello,", sys.argv[1])
except IndexError:
    print("Usage: notes.py Name or \"First name Last name\"")
"""

"""
if len(sys.argv) < 2:
    sys.exit("Too few args")
if len(sys.argv) > 2:
    sys.exit("Too many args")

print("Hello,", sys.argv[1])
"""

"""
#slice
for arg in sys.argv[1:]:
    print("Hello,", arg)
"""

#packages: pypi.org
#install with pip
"""
import cowsay as c
import sys

if len(sys.argv) == 2:
    c.cow("Hello, " + sys.argv[1])

"""

#APIs

import json
import requests as r
import sys

if len(sys.argv) != 2:
    sys.exit("Enter argument")

url = "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]

response = r.get(url)

#print(response.json())
#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])


#PEP 8

use pylint