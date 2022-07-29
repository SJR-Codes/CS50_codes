"""
* CS50P Problem Set 8
* Notes for OOP: Classes
* by Samu Reinikainen 29.07.2022
"""

class Student:
    #instance method to initialize
    def __init__(self, name, house):
        self.name = name
        self.house = house

    #make object pretty print itself
    def __str__(self):
        return f"Student: {self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    #@staticmethod

class professor:
    #instance method to initialize
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()