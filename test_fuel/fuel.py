def main():
    ...


def convert(fract):
    if(fract.count("/") == 1):
        fract = fract.split("/")
    else:
        raise ValueError

    try:
        x = int(fract[0])
        y = int(fract[1])
    except ValueError:
        #print("Value Error: Not valid fraction!")
        return False

    if y == 0:
        raise ZeroDivisionError

    if y <= 0 or x < 0 or x > y:
        #print("Zero or Negative Number Error: Not valid fraction!")
        return False

    return fract

def gauge(percentage):
    #convert fract to gauge, ie. 3/4 = 75%
    res = round(int(fract[0]) / int(fract[1]) * 100)

    if res <= 1:
        res = "E"
    elif res >= 99:
        res = "F"
    else:
        res = str(res) + "%"

    return res


if __name__ == "__main__":
    main()
