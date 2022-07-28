import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if m := re.search("^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        for e in m.groups():
            if int(e) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()