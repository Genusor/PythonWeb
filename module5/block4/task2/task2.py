import csv
rows = []
with open("m5-buckwheat.csv") as fp:
    reader = csv.reader(fp)
    for row in reader:
        rows.append(row)
fields = rows[0]
rows = rows[1:]
print(fields)
print(rows)
mins=[]
for e in rows:
    mins.append(e[1])
q=float(min(mins))/4
print(q)
