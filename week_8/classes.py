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
    def __init__(self, name, house, foobar=None):
        #houses = ["Foo","Bar","Huu","Haa"]
        #if not name:
        #    raise ValueError("Missing name")
        #not needed anymore cause we have setter for house
        #if house not in houses:
        #    raise ValueError("Invalid house")

        self.name = name
        self.house = house
        self.foobar = foobar

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

    def huuhaa(self):
        if self.foobar:
            return f"Action: {self.foobar}"
        else:
            return "Nothing happens..."

def main():
    #while True:
        #try:
    student = get_student()
        #except ValueError:
        #    ...
    #print(f"{student.name} from {student.house}")
    #using objects __str__ -method

    #using properties to prevent messing things like
    #student.house = "Gugguuu" #which bypass __init__ error checking
    #but now we can do this
    #student._house = "Gugguuu" #which bypass __init__ error checking

    print(student)
    #print(student.huuhaa())

def get_student():
    #create object/instance from class
    #student = Student()
    #set objects attributes / instance variables
    #student.name = input("Name: ")
    #student.house = input("House: ")

    name = input("Name: ")
    house = input("House: ")
    #foobar = input("foobar: ")

    #student = Student(name, house)
    #return student

    #return Student(name, house, foobar)
    return Student(name, house)

if __name__ == "__main__":
    main()