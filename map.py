"""
* CS50P Problem Set 8
* Notes week 9: function map, functional programming
* by Samu Reinikainen 30.07.2022
"""

def main():
    #yell("This is CS50")
    #yell(["This", "is", "CS50"])
    yell("This", "is", "CS50")


#def yell(phrase):
#    print(phrase.upper())
"""
def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
"""

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
