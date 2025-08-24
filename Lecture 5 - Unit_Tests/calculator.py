def main():
    x = int(input("What's x? "))
    print("Square of x is", square(x))


def square(n):
    return n * n
    # return n ** 2 # set the power
    # return pow(n , 2)


if __name__ == "__main__":
    main()
