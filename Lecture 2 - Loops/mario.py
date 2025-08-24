#----------------------Printing #'s in a Column-----------#

# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

#----------
# def main():
#     print_column(3)

# # def print_column(height):
# #     for _ in range(height):
# #         print("#")

# def print_column(height):
#     print("#\n" * height, end="")


# main()

#-------------Printing ?'s in a Row------------#

# def main():
#     print_rows(4)

# def print_rows(width):
#     print("?" * width)

# main()

#-------------Printing Square (Rows and Columns) ---------#

def main():
    print_square(3)

# def print_square(size):
#     for i in range(size):
#         print("#" * size)

def print_square(size):
    for i in range(size): # for each row in square
        for j in range(size): # for each brick in a row
            print("#", end="") # print brick
        print()

main()