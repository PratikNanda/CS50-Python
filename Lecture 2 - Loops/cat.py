# print ("meow\n" * 3, end="")

#---------------------WHILE LOOPS--------------------------#

# i = 0
# while i < 3:
#     print ("meow")
#     i += 1

# i = 1
# while i <= 3:
#     print ("meow")
#     i = i + 1   

# i = 3
# while i != 0:
#     print ("meow")
#     i = i - 1

#----------------------FOR LOOPS---------------------------#

# for _ in range(3):
#     print ("meow")

# for i in range(3):
#     print ("meow")

# for i in [2, 1, 2]:
#     print ("meow")

#--------With User input-----------------------#

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


#-----------------With Functions-----------------#

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:  
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()
        