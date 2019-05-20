from sklearn.neighbors import KNeighborsClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities
import matplotlib.pyplot as plt


pathFile = "../spambase.data"
better = 0
worst = 0
nbTurns = 10
nbNeighbors=2


result = {}





for tour in range(nbTurns):

    best = 0
    nbBest = 0

    print("Tour No : ")
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

            #if k not in [27, 28, 31, 57, 3, 19, 21, 22 ,26, 29, 30, 31, 32, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 49]:
            if k in [56, 55, 54]:
                listLine.append(line[k])
        usedValue.append(line[-1])
        usedData.append(listLine)
    '''data = np.array(data)
    print(data)
    '''


    testSetX = []
    testSetY = []
    for k in range (24):
        placeToTakeForTest = int(random() * len(usedData))
        x = usedData.pop(placeToTakeForTest)
        y = usedValue.pop(placeToTakeForTest)
        testSetX.append(x)
        testSetY.append(y)


    for nbNeighbors in range(1,50, 2):


        usedData = np.array(usedData)
        usedValue = np.array(usedValue)
        testSetX = np.array(testSetX)
        testSetY = np.array(testSetY)

        clf = KNeighborsClassifier(n_neighbors=nbNeighbors, weights="distance")
        clf = clf.fit(usedData, usedValue)
        value1 = clf.score(testSetX, testSetY)

        if value1 > best:
            best = value1
            nbBest = nbNeighbors
        #print("nb neighbors")
        #print(nbNeighbors)
        print(clf.predict(testSetX))



    print("Resultats : ")
    print(testSetY)
    print("best nb : ")
    print(nbBest)
    print(best)
    if nbBest in result:
        result[nbBest] += 1
    else:
        result[nbBest] = 1



print("\n")
print("Results : ")
print(result)


