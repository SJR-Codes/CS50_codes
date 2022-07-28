import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search("^[0-2]?[0-9]?[0-9]]\.[0-255]\.[0-255]\.[0-255]\$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()