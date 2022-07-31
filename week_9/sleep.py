"""
* CS50P Problem Set 9
* Notes week 9: generators
* by Samu Reinikainen 31.07.2022
"""

def main():
    n = int(input("Give n: "))

    for i in range(n):
        print("🐑" * (i+1))

def sheep(n):
    for i in range(n):
        print("🐑" * (i+1))

if __name__ == "__main__":
    main()