# email = input("What's your email? ").strip()

# # if "@" in email and "." in email:
# #     print("Valid")
# # else:
# #     print("Invalid")


# username, domain = email.split("@")

# # if username and "." in domain:
# #     print("Valid")
# # else:
# #     print("Invalid")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")



# -----------------------------------re Library ------------------------------------------------------

import re

email = input("What's your email? ").strip()

#if re.search("@", email):  
#if re.search(".+@.+", email):
#if re.search(".*@.*", email):
# if re.search(".+@.+.edu", email):
# if re.search(r".+@.+\.edu", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email):
# if re.search(r"^\w+@\w+\.(edu|com|gov|net)$", email):


# .lower() function to lowercase the input . You can use while taking input (name.strip().lower()) or in if like this if re.search("@", email.lower()):
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# re.match()
# re.fullmatch()