from sklearn.neighbors import KNeighborsClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities as drawSimilarities1
from analyse_stats.draw_class_repartition import drawSimilarities as drawSimilarities2
import matplotlib.pyplot as plt


pathFile = "../spambase.data"
better = 0
worst = 0
nbTurns = 20
nbNeighbors=2
weightValue = "distance"
totMod1 = 0
totMod2 = 0
totNonMod = 0
precision = 0.3
valueToCompare = 0.001

goodLines1 = drawSimilarities1(range(57), 2, valueToCompare, pathFile, False)
goodLines2 = drawSimilarities2(range(57), precision, valueToCompare, pathFile, False)
print(goodLines1)
print(goodLines2)



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

    clf = KNeighborsClassifier(n_neighbors=nbNeighbors, weights = weightValue )
    clf = clf.fit(usedData, usedValue)
    value1 = clf.score(testSetX, testSetY)




    ### Sorting type 1



    usedData = []
    usedValue = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in goodLines1 and k not in [27, 28, 31, 57]:
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

    clf = KNeighborsClassifier(n_neighbors=nbNeighbors, weights= weightValue)
    clf = clf.fit(usedData, usedValue)
    value2 = clf.score(testSetX, testSetY)



    ### Sorting type 2



    usedData = []
    usedValue = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in goodLines2 and k not in [27, 28, 31, 57]:
                # if k not in [27, 28, 31, 57]:
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

    clf = KNeighborsClassifier(n_neighbors=nbNeighbors, weights=weightValue)
    clf = clf.fit(usedData, usedValue)
    value3 = clf.score(testSetX, testSetY)





    print('Values : ')
    print(value1)
    print(value2)
    print(value3)

    totMod2 += value3
    totMod1 += value2
    totNonMod += value1

    if value1>value3:
        worst += 1
    else:
        better += 1

print("\n")
print("Percent of better")
print((better/nbTurns)*100)
print("Percent of worst ")
print((worst/nbTurns)*100)
print("\n")
print("Average of non modulated")
print(totNonMod/nbTurns)
print("Average of modulated type 1")
print(totMod1/nbTurns)
print("Average of modulated type 2")
print(totMod2/nbTurns)

'''
plt.figure()
plt.title('Word nb = ' )
labels = "mieux", "moins bien"
sizes = [(better/nbTurns)*100,(worst/nbTurns)*100]
colors = ['yellowgreen', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig('PieChart01.png')
plt.show()'''
