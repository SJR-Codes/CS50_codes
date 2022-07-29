"""
* CS50P Problem Set 8
* Notes for OOP: Classes
* by Samu Reinikainen 29.07.2022
"""

#
#class Student:
#    ...

class Student:

    #instance method to initialize
    def __init__(self, name, house):
        self.name = name
        self.house = house

    #make object pretty print itself
    def __str__(self):
        return f"Student: {self.name} from {self.house}"

    @property
    def name(self):
        #use underscore so variables and method name don't collide
        return self._name
    #setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    #getter property with decorators
    @property
    def house(self):
        #use underscore so variables and method name don't collide
        return self._house
    #setter
    @house.setter
    def house(self, house):
        houses = ["Foo","Bar","Huu","Haa"]
        if house not in houses:
            raise ValueError("Invalid house")
        else:
            #use underscore so variables and method name don't collide
            self._house = house

    #class methods
    #@classmethod
    #

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()