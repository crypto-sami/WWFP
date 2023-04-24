import csv
list_average=[]
list_high=[]
list_low=[]

with open('results.csv') as file:
    read = csv.reader(file, delimiter=',')
    data = []
    for row in read:
        data.append(row)

def test_avg(results, test):
    count = 0
    score = 0
    for i in range(len(results)):
        score +=int(results[i][test])
        count +=1
    avg = score/count
    list_average.append(avg)
    return(avg)

def high_score(results, test):
    score = 0
    for i in range(len(results)):
        if int((results[i][test])) > score:
            score = int((results[i][test]))
    list_high.append(score)
    return(score)

def low_score(results, test):
    score = 100
    for i in range(len(results)):
        if int((results[i][test])) < score:
            score = int((results[i][test]))
    list_low.append(score)
    return(score)

test_num=len(data[1])-1

for i in range(test_num):
    test_avg(data, i+1)
    high_score(data, i+1)
    low_score(data, i+1)


