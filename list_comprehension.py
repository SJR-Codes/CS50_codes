"""
* CS50P Problem Set 8
* Notes week 9: list comprehension
* by Samu Reinikainen 30.07.2022
"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
