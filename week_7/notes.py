"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

email = input("Give me your email: ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")