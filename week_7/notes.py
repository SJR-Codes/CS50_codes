"""
* CS50P Problem Set 7
* Notes for regexps
* by Samu Reinikainen 28.07.2022
"""

import re

email = input("Give me your email: ").strip()

"""
\d decimal digit
\D NOT decimal

\s whitespace (space, tab...)
\S NOT whitespace

\w word (with numbers and underscore)
\W NOT word

"""

# everything except @-sign [^@]
#if re.search("^[^@]+@[^@]+\.[a-zA-Z0-9]+$", email):

#if re.search("^[a-öA-Ö0-9_]+@[a-öA-Ö0-9_]+\.[a-öA-Ö0-9_]+$", email):

# \w = word or \W = not word
if re.search("^\w+@\w+\.\w+$", email):
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