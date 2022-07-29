"""
* CS50P Problem Set 8
* Notes for OOP: operator overloading
* by Samu Reinikainen 29.07.2022
"""

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"Vault has: {self.galleons} galls, {self.sickles} sickles, {self.knuts} knuts"

    #operator
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        return Vault(galleons, sickles, knuts)


potter = Vault(100,50,20)
print(potter)

weas = Vault(10,20,30)
print(weas)

#how to do this with operator overloading
#galls = potter.galleons + weas.galleons
#sickles = potter.sickles + weas.sickles
#knuts = potter.knuts + weas.knuts
#total = Vault(galls, sickles, knuts)

#+-operator overloaded in class __add__
total = potter + weas
print(total)