def main():
    print(hello(input("Who you? ")))

def hello(to="world"):
    #print("Hello,", to)
    return f"Hello, {to}"

if __name__ == "__main__":
    main()