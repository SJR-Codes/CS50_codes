"""
* CS50P Problem Set 8
* Notes for OOP
* by Samu Reinikainen 29.07.2022
"""


def main():
    #using tuple or list:
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")

    #return two values as tuple (inmutable)
    #return (name, house)

    #return two values as list (if you want to change values)
    return [name, house]

if __name__ == "__main__":
    main()