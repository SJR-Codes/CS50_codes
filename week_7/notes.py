"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

email = input("Give me your email: ").strip()

username, domain = email.split("@")

if len(username) > 1 and "." in domain:
    print("Valid")
else:
    print("Invalid")

"""
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""