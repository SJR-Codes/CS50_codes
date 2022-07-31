import random

class Hat:
    #def __init__(self):
    #    self.houses = ["Foo","Bar","Huu","Haa"]
    #class variables
    houses = ["Foo","Bar","Huu","Haa"]

#    def sort(self, name):
#        print(name, "is in", random.choice(self.houses))


    #class methods
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


#
#hat = Hat()
#hat.sort("Harry")

#when using class methods you can use class without initializing
Hat.sort("Harry")
