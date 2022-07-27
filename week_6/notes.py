"""
* CS50P Problem Set 6
* Notes for week 6
* by Samu Reinikainen 27.07.2022
"""

def main():
    names = []

    for _ in range(3):
        name = input("Your name: ")
        print(f"Hello, {name}")
        names.append(name)

    print(names)

if __name__ == "__main__":
    main()
