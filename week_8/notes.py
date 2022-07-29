"""
* CS50P Problem Set 8
* Notes for OOP
* by Samu Reinikainen 29.07.2022
"""


def main():
    student = get_student()

    #using tuple or list:
    #print(f"{student[0]} from {student[1]}")

    #using dict:
    print(f"{student[0]} from {student[1]}")

def get_student():
    #name = input("Name: ")
    #house = input("House: ")

    #return two values as tuple (inmutable)
    #return (name, house)

    #return two values as list (if you want to change values)
    #return [name, house]

    #return two values as list (if you want to change values)
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return {student}

if __name__ == "__main__":
    main()