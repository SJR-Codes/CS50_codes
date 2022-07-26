from calc import square

def main():
    test_square()

    print("All tests run.")

def test_square():
    """
    if square(2) != 4:
        print("Error: 2 squared != 4")
    if square(3) != 9:
        print("Error: 3 squared != 9")
    """
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()