from sklearn.naive_bayes import GaussianNB
from random import random
from importation import importcsv
import numpy as np




# Load data
rowData = importcsv()
data = []
for line in rowData:
    listLine = []
    for value in  line:
        listLine.append(float(value))
    data.append(listLine)

usedData = []
usedValue = []
for line in data:
    listLine = []
    for k in range(len(line)):
        if k != 27 and k != 28 and k != 31 and k!=57:
            listLine.append(line[k])
    usedValue.append(line[-1])
    usedData.append(listLine)
'''data = np.array(data)
print(data)
'''


testSetX = []
testSetY = []
for k in range (1000):
    placeToTakeForTest = int(random() * len(usedData))
    x = usedData.pop(placeToTakeForTest)
    y = usedValue.pop(placeToTakeForTest)
    testSetX.append(x)
    testSetY.append(y)


usedData = np.array(usedData)
usedValue = np.array(usedValue)
testSetX = np.array(testSetX)
testSetY = np.array(testSetY)

print(usedData[:1])
clf = GaussianNB()
clf = clf.fit(usedData, usedValue)
print(clf.score(usedData, usedValue))
#a = clf.predict(testSetX)
#print(a)
#print(testSetY)t

'''good = 0
bad = 0
for k in range(len(a)):
    if a[k] == testSetY[k]:
        good+=1
    else:
        bad+=1

print((good/(good+bad))*100)
print((bad/(good+bad))*100)
'''