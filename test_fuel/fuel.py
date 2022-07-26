def main():
    x = (input("Enter fraction (x/y, ie. 3/4): "))
    print(gauge(convert(x)))


def convert(fract):
    if(fract.count("/") == 1):
        fract = fract.split("/")
    else:
        raise ValueError

    if fract[0].isdigit():
        x = int(fract[0])
    else:
        raise ValueError

    if fract[1].isdigit():
        y = int(fract[1])
    else:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    return round(x / y * 100)

def gauge(percentage):
    return "X"
    try:
        percentage = int(percentage)
    except ValueError:
        return ""

    if percentage <= 1:
        res = "E"
    elif percentage >= 99:
        res = "F"
    else:
        res = str(percentage) + "%"

    return res


if __name__ == "__main__":
    main()
