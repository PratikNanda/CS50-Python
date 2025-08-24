# name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ") #split(", ?") doesn't work
#     name = f"{first} {last}"

# print(f"hello, {name}")


# import re

# name = input("What's your name? ").strip()
# # matches = re.search(r"^(.+), (.+)$", name)
# # matches = re.search(r"^(.+), ?(.+)$", name)
# matches = re.search(r"^(.+), *(.+)$", name)



# # if matches:
# #     last, first = matches.groups()
# #     name = f"{first} {last}"

# # if matches:
# #     last = matches.group(1)
# #     first = matches.group(2)
# #     name = f"{first} {last}"

# if matches:
#     name = matches.group(2) + " " + matches.group(1)


# print(f"hello, {name}")


# ---------------------With Walrus Operator ---------------------------------------

import re

name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")