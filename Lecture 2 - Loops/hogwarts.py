#---------LISTS-------------------#

# students = ["Hermione", "Harry", "Ron"]
# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# for i in range(3):  # if we know the length of list
#     print(students[i]) 

# for i in range(len(students)):
#     print(i + 1, students[i])

#--------------DICT---------------------------#

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# students = {"Hermione": "Gryffindor",
#             "Harry": "Gryffindor",
#             "Ron": "Gryffindor",
#             "Draco": "Slytherin"
#             }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")

# -------------Using Dictionaries and list as Tables---------#

students = [
    { "name": "Hermione", "house": "Gryffindor", "patronous": "Otter"},
    { "name": "Harry", "house": "Gryffindor", "patronous": "Stag"},
    { "name": "Ron", "house": "Gryffindor", "patronous": "Jack Russel Terrier"},
    { "name": "Draco", "house": "Slytherin", "patronous": None},
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")