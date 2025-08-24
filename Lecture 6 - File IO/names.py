# name = input("What's your name? ")
# print(f"hello, {name}")



# --------------for multiple values 

# names = []

# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)

#     other way

# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")


# =================How to save in python ?================

## Saves only one, because file = open("names.txt", "w") recreates a file
# name = input("What's your name? ")

# file = open("names.txt", "w")
# file.write(name)
# file.close()

## code for appended the values 

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()




