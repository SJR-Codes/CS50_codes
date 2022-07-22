"""
* CS50P Problem Set 1
* Deep Thought
* by Samu Reinikainen 22.07.2022
"""


answer = input("What is the answer to the meaning of life etc.? ")

if type(answer) == "int" and int(answer) == 42:
    print("Yes")
elif lower(answer) == "forty-two" or lower(answer) == "forty two":
    print("Yes")
else:
    print("No")
