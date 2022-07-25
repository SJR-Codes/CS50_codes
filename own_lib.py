def main():
    hello("world")
    goodbye("world")


def hello(name):
    print("Hello,", name)


def goodbye(name):
    print("Goodbye,", name)


# run main only when this file is run on it's own, not when imported
if __name__ == "__main__":
    main()
