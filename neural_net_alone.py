from sklearn.neural_network import MLPClassifier
from random import random
from importation import importcsv
import numpy as np

# Load data
rowData = importcsv()
data = []
for line in rowData:
    listLine = []
    for value in line:
        listLine.append(float(value))
    data.append(listLine)

usedData = []
usedValue = []
for line in data:
    listLine = []
    for k in range(len(line)):
        if k != 27 and k != 28 and k != 32 and k != 57:
            listLine.append(line[k])
    usedValue.append(line[-1])
    usedData.append(listLine)
'''data = np.array(data)
print(data)
'''

testSetX = []
testSetY = []
for k in range(100):
    placeToTakeForTest = int(random() * len(usedData))
    x = usedData.pop(placeToTakeForTest)
    y = usedValue.pop(placeToTakeForTest)
    testSetX.append(x)
    testSetY.append(y)

usedData = np.array(usedData)
usedValue = np.array(usedValue)
testSetX = np.array(testSetX)
testSetY = np.array(testSetY)

bestValue = [0, None, None]

for nbLayer in range(150, 300, 5):
    for alphaValue in [0.0001] :#, 0.00001, 0.0001, 0.001, 0.01, 0.1]:
        print('\n New test : ')
        print('nb layers : ')
        print(nbLayer)
        print('And alpha : ')
        print(alphaValue)
        #print(usedData[:1])
        clf = MLPClassifier(hidden_layer_sizes=(nbLayer, ), alpha=alphaValue)
        clf = clf.fit(usedData, usedValue)
        a = clf.score(testSetX, testSetY)
        print(a)
        if a>bestValue[0]:
            bestValue = [a, alphaValue, nbLayer]

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



print('best values : ')
print(bestValue)