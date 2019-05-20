from sklearn import tree
from random import random
from ImportCsv import importcsv
import numpy as np




# Load data

rowData = importcsv("../spambase.data")
data = []
for line in rowData:
    listLine = []
    for value in  line:
        listLine.append(float(value))
    data.append(listLine)


#print(data[0])
#print(len(data))

#### Specific fields####
usedData = []
usedValue = []
usedData1 = []
usedValue1 = []
for line in data:
    listLine = []
    listLine1 = []
    for k in range(len(line)):
        #if k in [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 46, 51, 52, 53]:
        if k in [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 37, 46, 51, 52, 53] and k not in [27, 28, 31, 57]:
            listLine.append(line[k])
        if k != 27 and k != 28 and k != 31 and k!=57:
            listLine1.append(line[k])
    usedValue.append(line[-1])
    usedData.append(listLine)
    usedValue1.append(line[-1])
    usedData1.append(listLine1)
'''data = np.array(data)
print(data)
'''


testSetX = []
testSetY = []
testSetX1 = []
testSetY1 = []
for k in range (20):
    placeToTakeForTest = int(random() * len(usedData))
    x = usedData.pop(placeToTakeForTest)
    y = usedValue.pop(placeToTakeForTest)
    testSetX.append(x)
    testSetY.append(y)
    x = usedData1.pop(placeToTakeForTest)
    y = usedValue1.pop(placeToTakeForTest)
    testSetX1.append(x)
    testSetY1.append(y)





usedData1 = np.array(usedData1)
usedValue1 = np.array(usedValue1)
testSetX1 = np.array(testSetX1)
testSetY1 = np.array(testSetY1)

#print(usedData[:1])
clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(usedData1, usedValue1)
print("Everything")
#print(clf1.score(testSetX1, testSetY1))
print(clf1.predict(testSetX1))


usedData = np.array(usedData)
usedValue = np.array(usedValue)
testSetX = np.array(testSetX)
testSetY = np.array(testSetY)

#print(usedData[:1])
clf = tree.DecisionTreeClassifier()
clf = clf.fit(usedData, usedValue)
print("Specific")
#print(clf.score(testSetX, testSetY))
print(clf.predict(testSetX))

print('jjj')
print(testSetY)





#a = clf.predict(testSetX)
#print(a)
#print(testSetY)
'''
good = 0
bad = 0
for k in range(len(a)):
    if a[k] == testSetY[k]:
        good+=1
    else:
        bad+=1

print((good/(good+bad))*100)
print((bad/(good+bad))*100)'''
