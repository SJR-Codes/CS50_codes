import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if m := re.search("^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if m.group(1) <= 255 and m.group(2) <= 255 and m.group(3) <= 255 and m.group(4) <= 255:
            return True
    else:
        return False


if __name__ == "__main__":
    main()