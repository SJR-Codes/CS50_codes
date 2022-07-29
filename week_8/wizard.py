"""
* CS50P Problem Set 8
* Notes for OOP: Classes
* by Samu Reinikainen 29.07.2022
"""

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Invalid name")
        self.name = name

class Student(Wizard):
    #instance method to initialize
    def __init__(self, name, house):
        #calling parent class
        super().__init__(name)
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

class Professor(Wizard):
    #instance method to initialize
    def __init__(self, name, subject):
        #calling parent class
        super().__init__(name)
        self.subject = subject

def main():
    wizard = Wizard("Albus")
    prof = Professor("Albus")
    student = Student("Harry")
    print(student)

if __name__ == "__main__":
    main()