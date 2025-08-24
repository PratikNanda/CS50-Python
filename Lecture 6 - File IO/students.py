# with open ("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# ----------------------------------------------------------------------------------------

# with open ("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")


# ----------------------------------------------------------------------------------------

# students = []

# with open ("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

# ------------------------------sorting by students name----------------------------------------------------------
# students = []

# with open ("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house

#         student = {"name": name, "house": house} # dictionary in single step

#         students.append(student)

# # def get_name(student):
# #     return student["name"]

# # for student in sorted(students, key = get_name):
# #     print(f"{student['name']} is in {student['house']}")

# # --------------------using lambda ---------------------------------------

# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# --------------------------------------------------------------
# students.csv changed
# house changed to home and Hermione is removed

# Hermione,Gryffindor
# Harry,Gryffindor
# Ron,Gryffindor
# Draco,Slytherin

students = []

with open ("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")

        student = {"name": name, "home": home} # dictionary in single step

        students.append(student)

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")