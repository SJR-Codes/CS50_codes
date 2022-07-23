"""
* CS50P Problem Set 2
* Vanity Plates
* by Samu Reinikainen 23.07.2022
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #“All vanity plates must start with at least two letters.”
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    #“No periods, spaces, or punctuation marks are allowed.”


def has_two_start(s):
    #check that first two chars are letters

def has_corr_amount(s):
    #check that string len is 2-6
    return 6 >= s.len() >= 2

main()