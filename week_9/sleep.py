"""
* CS50P Problem Set 9
* Notes week 9: generators
* by Samu Reinikainen 31.07.2022
"""
"""
def main():
    n = int(input("Give n: "))

    for s in sheep(n):
        print(s)
#million sheep stalls computer

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * (i+1))

    return flock
"""


def main():
    n = int(input("Give n: "))

    for s in sheep(n):
        print(s)

#using generators, yield, iterators
#if printing millions of sheep, normal return stalls comp 'cause it's trying to return million * million sheep
#yield returns 1 row at time
def sheep(n):
    for i in range(n):
        yield "🐑" * (i+1)


if __name__ == "__main__":
    main()