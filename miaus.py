"""
* CS50P Problem Set 8
* Notes week 9: Constants
* by Samu Reinikainen 30.07.2022
"""

"""
#no constans in python to prevent MIAUS changed after declaring
MIAUS = 3

for _ in range(MIAUS):
    print("Miau!")
"""

class Cat:
    MIAUS = 3

    def miau(self):
        for _ in range(Cat.MIAUS):
            print("Miau!")

cat = Cat()
cat.miau()