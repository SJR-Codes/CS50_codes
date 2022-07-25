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

number = r.randint(1,10)

print(number)

cards = ["Jack", "Queen", "King", "Ace"]
print(cards)
r.shuffle(cards)
for card in cards:
    print(card)