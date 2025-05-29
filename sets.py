import csv


studs = []

with open("students.csv") as doc:
    deets = csv.DictReader(doc)
    for deet in deets:
        studs.append(deet)


houses = set()
for stud in studs:
    houses.add(stud["house"])


for house in sorted(houses):
    print(house)