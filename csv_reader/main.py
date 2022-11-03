import csv
import matplotlib.pyplot as plt

f = open("csv_reader/Daten_Informatik_csv.csv", encoding = "UTF-8")

csv_reader = csv.reader(f, delimiter = ";")

datum = []
schritte = []

for i, line in enumerate(csv_reader):
    print(i)
    if i != 0:
        datum.append(line[0])
        schritte.append(int(line[2]))

print(datum)
f.close()

plt.plot(datum, schritte)
plt.xlabel("Datum")
plt.ylabel("Schritte")
plt.show()