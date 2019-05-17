from sklearn.neighbors import KNeighborsClassifier
from random import random
from importation import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities
import matplotlib.pyplot as plt


pathFile = "spambase.data"
better = 0
worst = 0
nbTurns = 100
for tour in range(nbTurns):
    print(tour)
    # Load data
    rowData = importcsv(pathFile)
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
            #if k in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 37, 46, 48, 50, 51, 52, 53] and k not in [27, 28, 31, 57]:
            if k not in [27, 28, 31, 57]:
                listLine.append(line[k])
        usedValue.append(line[-1])
        usedData.append(listLine)
    '''data = np.array(data)
    print(data)
    '''


    testSetX = []
    testSetY = []
    for k in range (100):
        placeToTakeForTest = int(random() * len(usedData))
        x = usedData.pop(placeToTakeForTest)
        y = usedValue.pop(placeToTakeForTest)
        testSetX.append(x)
        testSetY.append(y)


    usedData = np.array(usedData)
    usedValue = np.array(usedValue)
    testSetX = np.array(testSetX)
    testSetY = np.array(testSetY)

    clf = KNeighborsClassifier()
    clf = clf.fit(usedData, usedValue)
    value1 = clf.score(testSetX, testSetY)


    goodLines = drawSimilarities(range(57), 2, 0.03, pathFile, False)
    usedData = []
    usedValue = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in goodLines and k not in [27, 28, 31, 57]:
            #if k not in [27, 28, 31, 57]:
                listLine.append(line[k])
        usedValue.append(line[-1])
        usedData.append(listLine)
    '''data = np.array(data)
    print(data)
    '''


    testSetX = []
    testSetY = []
    for k in range (100):
        placeToTakeForTest = int(random() * len(usedData))
        x = usedData.pop(placeToTakeForTest)
        y = usedValue.pop(placeToTakeForTest)
        testSetX.append(x)
        testSetY.append(y)


    usedData = np.array(usedData)
    usedValue = np.array(usedValue)
    testSetX = np.array(testSetX)
    testSetY = np.array(testSetY)

    clf = KNeighborsClassifier()
    clf = clf.fit(usedData, usedValue)
    value2 = clf.score(testSetX, testSetY)

    if value1>value2:
        worst += 1
    else:
        better += 1


print((better/nbTurns)*100)
print((worst/nbTurns)*100)


plt.figure()
plt.title('Word nb = ' + str(placeOfWordToCompare))
labels = "mieux", "moins bien"
sizes = [(better/nbTurns)*100,(worst/nbTurns)*100]
colors = ['yellowgreen', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig('PieChart01.png')
plt.show()

