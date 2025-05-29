import csv

students =[]

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row) # students.append({"name": row["name"], "home": row["home"]})
# 
#key=lambda student: student["name"]): is an alternative to creating a one-time function 


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

x= 35
y = 40 
print(x+y)