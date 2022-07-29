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
    def __init__(self, name, house, foobar):
        houses = ["Foo","Bar","Huu","Haa"]
        if not name:
            raise ValueError("Missing name")
        if house not in houses:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house
        self.foobar = foobar

    #make object pretty print itself
    def __str__(self):
        return f"Student: {self.name} from {self.house}"

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
    print(student)
    print(student.huuhaa())

def get_student():
    #create object/instance from class
    #student = Student()
    #set objects attributes / instance variables
    #student.name = input("Name: ")
    #student.house = input("House: ")

    name = input("Name: ")
    house = input("House: ")
    foobar = input("foobar: ")

    #student = Student(name, house)
    #return student

    return Student(name, house, foobar)

if __name__ == "__main__":
    main()