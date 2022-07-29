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
        houses = ["Foo","Bar","Huu","Haa"]
        if not name:
            raise 
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    #create object/instance from class
    #student = Student()
    #set objects attributes / instance variables
    #student.name = input("Name: ")
    #student.house = input("House: ")

    name = input("Name: ")
    house = input("House: ")

    #student = Student(name, house)
    #return student

    return Student(name, house)

if __name__ == "__main__":
    main()