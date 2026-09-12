import csv

with open("joints.csv") as f:
    for row in csv.reader(f):
        print(row)

print("---- naive split")
with open("joints.csv") as f:
    for line in f:
        print(line.strip().split(","))
