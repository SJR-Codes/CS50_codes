"""
* CS50P Problem Set 6
* Notes for week 6
* by Samu Reinikainen 27.07.2022
"""

def main():
    names = []

    #for _ in range(3):
    name = input("Your name: ")
    #    names.append(name)

    #for name in sorted(names):
    #    print(f"Hello, {name}")

    filen = "names.txt"
    file = open(filen, "w")
    file.write(name)
    file.close

if __name__ == "__main__":
    main()
