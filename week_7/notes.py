"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

import re

email = input("Give me your email: ").strip()

if re.search(".*@.+", email):
    print("Valid")
else:
    print("Invalid")

#username, domain = email.split("@")

"""
if len(username) > 1 and "." in domain:
    print("Valid")
else:
    print("Invalid")
"""
"""
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""