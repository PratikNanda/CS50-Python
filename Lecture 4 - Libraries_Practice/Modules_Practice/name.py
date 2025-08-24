import sys

# print("hello, my name is",sys.argv[1])
# ----------------------------------------------
# try:
#     print("hello, my name is",sys.argv[1])

# except IndexError:
#     print("too few arguments")
# ----------------------------------------------


# if len(sys.argv) < 2:
#     print("too few arguments")
# elif len(sys.argv) > 2:
#     print("too many arguments")
# else:
#     print("hello, my name is",sys.argv[1]) # if you want full name in 1 argument then use " "

# -----------------sys.exit()---------------------

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("too many arguments")

# print("hello, my name is",sys.argv[1])

#----------------------------------------

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")

# for arg in sys.argv:
#     print("hello, my name is",arg)

#--------------------Slicer---------------

if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is",arg)

for arg in sys.argv[1:-1]:
    print("hello, my name is",arg)


