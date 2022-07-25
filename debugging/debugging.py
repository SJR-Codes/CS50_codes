"""
* CS50P Problem Set 3
* Debugging
* by Samu Reinikainen 24.07.2022
"""

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(h):
    for i in range(h):
        print("#" * i)

if __name__ == "__main__":
    main()
