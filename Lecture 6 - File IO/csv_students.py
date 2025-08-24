import csv

# -------------------------------------------------------------------------------------------------------
# students = []

# with open ("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
   
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# ------------------------------------------------------------------------------------------

# Writing in CSV

name = input("What's your name? ")
home = input("Where's your home? ")

with open("writeincsv.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})