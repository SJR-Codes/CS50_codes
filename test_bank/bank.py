"""
* CS50P Problem Set 1
* Home Federal Savings Bank
* by Samu Reinikainen 22.07.2022
"""

def main():
    print("$" + str(value(input("Greetings: ").lower())))


def value(greet):
    if greet[0:5] == "hello":
        return "0"
    elif greet[0] == "h":
        return "20"
    else:
        return "100"


if __name__ == "__main__":
    main()




