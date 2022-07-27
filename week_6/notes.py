"""
* CS50P Problem Set 6
* Notes for week 6
* by Samu Reinikainen 27.07.2022
"""

def main():
    names = []

    #for _ in range(3):
    name = input("Give name: ")
    foo = input("Foo bar: ")
    #    names.append(name)

    #for name in sorted(names):
    #    print(f"Hello, {name}")

    filen = "names.csv"
    #file = open(filen, "a") #w = write, a = append
    #file.write(name + "\n")
    #file.close()

    #pythonic way
    with open(filen, "a") as file:
        file.write(name + "," + foo + "\n")

    readfile()
"""
def readfile():
    filen = "names.txt"
    with open(filen, "r") as file:
        lines = file.readlines()

    for line in lines:
        print(f"Hello, {line}", end="")
"""

def readfile():
    filen = "names.csv"
    """
    filen = "names.txt"
    with open(filen, "r") as file:
        for line in file:
            print("Hello, ", line.rstrip())
    """

    """
    names = []
    with open(filen, "r") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"Hello, {name.title()}")

    """
    lines = []
    with open(filen, "r") as file:
        for line in file:
            lines.append(line.rstrip())

    for line in sorted(lines):
        row = line.rstrip().split(",")

        print(f"Hello, {row[0].title()} from {row[1]}")




if __name__ == "__main__":
    main()
