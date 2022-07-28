"""
* CS50P Problem Set 7
* Response Validation
* by Samu Reinikainen 28.07.2022
"""

from validator_collection import validators, errors

def main():
    #print(validate(input("What's your email address? ").strip()))
    print(check("ad@ad.fi"))


def check(e):

    if validators.email(e, allow_empty = False):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()