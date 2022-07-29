import random

class Hat:
    def __init__(self):
        self.houses = ["Foo","Bar","Huu","Haa"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


    #class methods
    #@classmethod


hat = Hat()

hat.sort("Harry")
