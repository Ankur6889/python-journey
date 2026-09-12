import csv

rows = [["name", "limit"], ["elbow", 10], ["wrist", 45]]

with open("out.csv", "w", newline="") as f:
    w = csv.writer(f)
    for row in rows:
        w.writerow(row)

print(repr(open("out.csv").read()))
