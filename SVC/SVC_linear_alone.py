from sklearn.neighbors import KNeighborsClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from sklearn.svm import SVC
from analyse_stats.draw_similarities_middle import drawSimilarities as drawSimilarities1
from analyse_stats.draw_class_repartition import drawSimilarities as drawSimilarities2
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

pathFile = "../spambase.data"
better = 0
worst = 0
nbTurns = 100
nbNeighbors = 2
weightValue = "distance"
ker = "linear"

dicoResult = {}
tot = 0
for tour in range(nbTurns):
    best = [0, 0]
    for nbWord in [0]:
        print(tour)
        # Load data
        rowData = importcsv(pathFile)
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
                #if k not in [27, 28, 31, 57, 3, 30, 32, 36, 39, 40, 46, 47]:
                if k in [0, 2, 55, 56]:
                    listLine.append(line[k])
            usedValue.append(line[-1])
            usedData.append(listLine)
        '''data = np.array(data)
        print(data)
        '''

        testSetX = []
        testSetY = []
        for k in range(250):
            placeToTakeForTest = int(random() * len(usedData))
            x = usedData.pop(placeToTakeForTest)
            y = usedValue.pop(placeToTakeForTest)
            testSetX.append(x)
            testSetY.append(y)

        usedData = np.array(usedData)
        usedValue = np.array(usedValue)
        testSetX = np.array(testSetX)
        testSetY = np.array(testSetY)

        scaler1 = StandardScaler()
        scaler1.fit(usedData)
        usedDataScale2 = scaler1.transform(usedData)
        testSetXScale2 = scaler1.transform(testSetX)



        clf = SVC(kernel=ker, C=0.2)
        clf = clf.fit(usedDataScale2, usedValue)
        # print("\n importance 1:")
        # print(clf.feature_importances_)
        #value1 = clf.score(testSetX, testSetY)
        valueScale1 = clf.score(testSetXScale2, testSetY)
        valueProba = clf.predict(testSetXScale2)
        print(valueProba)
        print(valueScale1)
        if valueScale1>best[0]:
            best = [valueScale1, nbWord]


        tot += valueProba

        if best[1] in dicoResult:
            dicoResult[best[1]] +=1
        else:
            dicoResult[best[1]] = 1


print(dicoResult)
print(best)
print(tot/nbTurns)








