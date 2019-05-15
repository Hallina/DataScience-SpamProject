from sklearn.neural_network import MLPClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities as drawSimilarities1
from analyse_stats.draw_class_repartition import drawSimilarities as drawSimilarities2
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier




pathFile = "../spambase.data"
better = 0
worst = 0
nbTurns = 100
nbNeighbors=2
weightValue = "distance"
totMod1 = 0
totMod2 = 0
totNonMod = 0
precision = 0.3
valueToCompare = 0.001
nbElementTest = 100

goodLines1 = drawSimilarities1(range(57), 2, valueToCompare, pathFile, False)
goodLines2 = drawSimilarities2(range(57), precision, valueToCompare, pathFile, False)
print(goodLines1)
print(goodLines2)

totGen = 0



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

    usedData1 = []
    usedValue1 = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in goodLines2 and k not in [27, 28, 31, 57]:
                # if k not in [27, 28, 31, 57]:
                listLine.append(line[k])
        usedValue1.append(line[-1])
        usedData1.append(listLine)
    '''data = np.array(data)
    print(data)
    '''



    testSetX = []
    testSetY = []
    testSetX1 = []
    testSetY1 = []
    for k in range (nbElementTest):
        placeToTakeForTest = int(random() * len(usedData))
        x = usedData.pop(placeToTakeForTest)
        y = usedValue.pop(placeToTakeForTest)
        testSetX.append(x)
        testSetY.append(y)
        x1 = usedData1.pop(placeToTakeForTest)
        y1 = usedValue1.pop(placeToTakeForTest)
        testSetX1.append(x1)
        testSetY1.append(y1)






    usedData = np.array(usedData)
    usedValue = np.array(usedValue)
    testSetX = np.array(testSetX)
    testSetY = np.array(testSetY)
    usedData1 = np.array(usedData1)
    usedValue1 = np.array(usedValue1)
    testSetX1 = np.array(testSetX1)
    testSetY1 = np.array(testSetY1)



    clf1 = AdaBoostClassifier(n_estimators = 200)
    clf1 = clf1.fit(usedData, usedValue)
    #print("\n importance 1:")
    #print(clf1.predict(testSetX))
    value1 = clf1.predict(testSetX)
    value1Score = clf1.score(testSetX, testSetY)
    #print(value1Score)

    clf2 = MLPClassifier()
    clf2 = clf2.fit(usedData, usedValue)
    #print("\n importance 2:")
    #print(clf2.predict(testSetX))
    value2 = clf2.predict(testSetX)
    value2Score = clf2.score(testSetX, testSetY)
    #print(value2Score)

    clf3 = KNeighborsClassifier(n_neighbors=nbNeighbors, weights=weightValue)
    clf3 = clf3.fit(usedData1, usedValue1)
    #print("\n importance 3:")
    #print(clf3.predict(testSetX1))
    value3 = clf3.predict(testSetX1)
    value3Score = clf3.score(testSetX1, testSetY1)
    #print(value3Score)

    #print("Et en vrai")

    #print(testSetY)

    result = []
    for k in range(nbElementTest):
        valTot = value1[k] + value2[k] + value3[k]
        if valTot == 1 or valTot == 0:
            result.append(0)
        else:
            result.append(1)

    goodChoices = 0
    for k in range(len(result)):
        if result[k] == testSetY[k]:
            goodChoices+=1

    #print("Au final : ")
    #print(goodChoices/len(result))

    totGen += goodChoices/len(result)

print(totGen/nbTurns)



