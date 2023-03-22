import csv
file = open('results.csv', 'r')
read = csv.reader(file, delimiter=';')
data = []
for row in read:
    data.append(row) 

print(data)