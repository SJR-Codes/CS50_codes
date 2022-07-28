"""
* CS50P Problem Set 7
* Numb3rs
* by Samu Reinikainen 28.07.2022
"""
import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if m := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for e in m.groups():
            if int(e) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()