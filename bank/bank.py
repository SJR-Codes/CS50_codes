"""
* CS50P Problem Set 1
* Home Federal Savings Bank
* by Samu Reinikainen 22.07.2022
"""


greet = input("Greetings: ").strip().lower()

if greet == "hello":
    print("0$")
elif greet[0] == "h":
    print("20$")
else:
    print("100$")
