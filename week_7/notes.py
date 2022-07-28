"""
* CS50P Problem Set 7
* Notes
* by Samu Reinikainen 28.07.2022
"""

email = input("Give me your email: ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")