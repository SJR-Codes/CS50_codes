"""
* CS50P Problem Set 8
* Notes week 9: unpacking
* by Samu Reinikainen 30.07.2022
"""

#unpacking variables to multiple vars

"""
#split return two but you want to use just one
first, _ = input("Name").split(" ")
print(f"Hello, {first}")
"""

def total(galleons, sickles, knuts):
    return (galleons * 17 +  sickles) * 29 + knuts
"""
coins = [100,50,25]

#the hard way
#print(total(coins[0],coins[1],coins[2]), "Knuts")

#unpacking list way with *
print(total(*coins), "Knuts")
"""

#named variables
print(total(galleons=100, sickles=50, knuts=25), "Knuts")

coins = {"sickles": 50, "galleons": 100, "knuts": 25}

#hard way
print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

#unpacking dictionary to named variables with **
print(total(**coins), "Knuts")