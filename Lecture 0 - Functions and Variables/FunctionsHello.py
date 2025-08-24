# def hello(to="World"):
#     print("hello, " , to)


# hello()
# name = input("What's your name? ")
# # print("hello, " , name)
# hello(name)

#-----With main function
def main():
    name = input ("What's your name? ").capitalize()
    hello(name)


def hello(to="World"):
    print("hello, " , to)

main()
