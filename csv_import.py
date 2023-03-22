import csv

with open('results.csv') as file:
    read = csv.reader(file, delimiter=',')
    data = []
    for row in read:
        data.append(row)

print(data)
print(data[0][0])