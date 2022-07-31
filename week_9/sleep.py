"""
* CS50P Problem Set 9
* Notes week 9: generators
* by Samu Reinikainen 31.07.2022
"""

def main():
    n = int(input("Give n: "))

    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * (i+1))

    return flock

if __name__ == "__main__":
    main()