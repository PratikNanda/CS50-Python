# ---- ValueError: invalid literal for int() with base 10: 'cat'
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an Integer")

#------ NameError: name 'x' is not defined--

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an Integer")
# else:
#     print(f"x is {x}")

# ----------Using Loops---------------

# while True:
#     try:
#         x = int(input("What's x? "))
#         # break    | uncomment this and remove else |
#     except ValueError:
#         print("x is not an Integer")
#     else:
#         break
# print(f"x is {x}")

#---------Using Functions-----------------

# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             # return int(input("What's x? "))
#             x = int(input("What's x? "))
#             return x
#         except ValueError:
#             print("x is not an Integer")
#         # else:
#             # return x  # return is stronger than break
#     #         break
#     # return x

# main()

#---------Pass Keyword ----------------

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
             return int(input(prompt))

        except ValueError:
            pass

main()


# raise expection