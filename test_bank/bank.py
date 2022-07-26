"""
* CS50P Problem Set 5
* Test Federal Savings Bank
* by Samu Reinikainen 26.07.2022
"""

def main():
    print("$" + value(input("Greetings: ")))


def value(greet):
    greet = str(greet).lower()
    if len(greet) < 1:
        return 100

    if greet[0:5] == "hello":
        return 0
    elif greet[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()




