"""
* CS50P Problem Set 1
* Meal Time
* by Samu Reinikainen 22.07.2022
"""


def main():
    utime = input("What time is it? ").strip()

    ctime = convert(utime)
    print(ctime)
"""
    match ctime:
        case 7:
            print("Breakfast")
        case
"""

def convert(time):
    tmp = time.split(":")

    return float(tmp[0] + (tmp[1]/60))


if __name__ == "__main__":
    main()