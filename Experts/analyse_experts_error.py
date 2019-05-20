from sklearn.neural_network import MLPClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities as drawSimilarities1
from analyse_stats.draw_class_repartition import drawSimilarities as drawSimilarities2
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree




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
nbElementTest = 20

goodLines1 = drawSimilarities1(range(57), 2, valueToCompare, pathFile, False)
goodLines2 = drawSimilarities2(range(57), precision, valueToCompare, pathFile, False)
#print(goodLines1)
#print(goodLines2)

totGen = 0
error = 0
listErrors = []
listOk = []



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


    clf2 = MLPClassifier()
    clf2 = clf2.fit(usedData, usedValue)
    #print("\n importance 2:")
    #print(clf2.predict(testSetX))
    value2 = clf2.predict(testSetX)
    value2Score = clf2.score(testSetX, testSetY)


    clf3 = KNeighborsClassifier(n_neighbors=nbNeighbors, weights=weightValue)
    clf3 = clf3.fit(usedData1, usedValue1)
    #print("\n importance 3:")
    #print(clf3.predict(testSetX1))
    value3 = clf3.predict(testSetX1)
    value3Score = clf3.score(testSetX1, testSetY1)


    clf4 = tree.DecisionTreeClassifier()
    clf4 = clf4.fit(usedData, usedValue)
    # print("\n importance 4:")
    #print(clf4.predict(testSetX))
    value4 = clf4.predict(testSetX)
    value4Score = clf4.score(testSetX, testSetY)

    '''print(value1Score)
    print(value2Score)
    print(value3Score)
    print(value4Score)'''

    #print("Et en vrai")



    result = []
    for k in range(nbElementTest):
        valTot = value1[k] + value2[k] + value4[k] #+ value3[k]
        #print(valTot)
        if valTot in [0,1]:
            #print('0')
            result.append(0)
        else:
            #print('1')
            result.append(1)

    goodChoices = 0
    for k in range(len(result)):
        if result[k] == testSetY[k]:
            goodChoices+=1

    #print("Au final : ")
    #print(result)
    #print(testSetY)

    for line in range(len(testSetX)):
        if int(result[line]) != int(testSetY[line]):
            error += 1
            listErrors.append(testSetX[line])
            #print(testSetX[line])
        else:
            listOk.append(testSetX[line])

    #print(goodChoices/len(result))

    totGen += goodChoices/len(result)


dictionnaireErreurs = {}
for k in range(len(listErrors[0])):
    dictionnaireErreurs[k] = 0

for errorRegistered in listErrors:
    for k in range(len(listErrors[0])):
        dictionnaireErreurs[k] += errorRegistered[k]/len(listErrors)




dictionnaireErreurs = {}
for k in range(len(listErrors[0])):
    dictionnaireErreurs[k] = 0

for errorRegistered in listErrors:
    for k in range(len(listErrors[0])):
        dictionnaireErreurs[k] += errorRegistered[k]


for key in dictionnaireErreurs :
    dictionnaireErreurs[key] /= len(errorRegistered)




dictionnaireBons = {}
for k in range(len(listOk[0])):
    dictionnaireBons[k] = 0

for OKRegistered in listOk:
    for k in range(len(listOk[0])):
        dictionnaireBons[k] += OKRegistered[k]

for key in dictionnaireBons :
    dictionnaireBons[key] /= len(OKRegistered)

for key in dictionnaireBons :

    a = dictionnaireErreurs[key] / len(errorRegistered)
    b = dictionnaireBons[key] / len(OKRegistered)
    if a>b*100 or b>100*a:
        print(key)
        print(a)
        print(b)

