import csv

with open('results.csv') as file:
    read = csv.reader(file, delimiter=',')
    data = []
    for row in read:
        data.append(row)

def test_avg(results, test, students):
    count = 0
    score = 0
    for i in range(students):
        score +=int(results[i][test])
        count +=1
    return(score/count)

def high_score(results, test, students):
    score = 0
    for i in range(students):
        if int((results[i][test])) > score:
            score = int((results[i][test]))
    return(score)

def low_score(results, test, students):
    score = 100
    for i in range(students):
        if int((results[i][test])) < score:
            score = int((results[i][test]))
    return(score)

