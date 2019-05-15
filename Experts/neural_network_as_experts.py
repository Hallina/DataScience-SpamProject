from sklearn.neural_network import MLPClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities as drawSimilarities1
from analyse_stats.draw_class_repartition import drawSimilarities as drawSimilarities2
import matplotlib.pyplot as plt


pathFile = "../spambase.data"
better = 0
worst = 0
nbTurns = 1
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


    ### Sorting type 1



    usedData1 = []
    usedValue1 = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in goodLines1 and k not in [27, 28, 31, 57]:
            #if k not in [27, 28, 31, 57]:
                listLine.append(line[k])
        usedValue1.append(line[-1])
        usedData1.append(listLine)
    '''data = np.array(data)
    print(data)
    '''




    ### Sorting type 2



    usedData2 = []
    usedValue2 = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in goodLines2 and k not in [27, 28, 31, 57]:
                # if k not in [27, 28, 31, 57]:
                listLine.append(line[k])
        usedValue2.append(line[-1])
        usedData2.append(listLine)
    '''data = np.array(data)
    print(data)
    '''

    testSetX = []
    testSetY = []
    testSetX1 = []
    testSetY1 = []
    testSetX2 = []
    testSetY2 = []

    for k in range(100):
        placeToTakeForTest = int(random() * len(usedData))
        x = usedData.pop(placeToTakeForTest)
        y = usedValue.pop(placeToTakeForTest)
        testSetX.append(x)
        testSetY.append(y)
        x1 = usedData1.pop(placeToTakeForTest)
        y1 = usedValue1.pop(placeToTakeForTest)
        testSetX1.append(x1)
        testSetY1.append(y1)
        x2 = usedData2.pop(placeToTakeForTest)
        y2 = usedValue2.pop(placeToTakeForTest)
        testSetX2.append(x2)
        testSetY2.append(y2)









    usedData = np.array(usedData)
    usedValue = np.array(usedValue)
    testSetX = np.array(testSetX)
    testSetY = np.array(testSetY)



    usedData1 = np.array(usedData1)
    usedValue1 = np.array(usedValue1)
    testSetX1 = np.array(testSetX1)
    testSetY1 = np.array(testSetY1)

    usedData2 = np.array(usedData2)
    usedValue2 = np.array(usedValue2)
    testSetX2 = np.array(testSetX2)
    testSetY2 = np.array(testSetY2)











    clf = MLPClassifier()
    clf = clf.fit(usedData, usedValue)
    print(clf.predict(testSetX))
    value1 = clf.score(testSetX, testSetY)

    clf = MLPClassifier()
    clf = clf.fit(usedData1, usedValue1)
    print(clf.predict(testSetX1))
    value2 = clf.score(testSetX1, testSetY1)

    clf = MLPClassifier()
    clf = clf.fit(usedData2, usedValue2)
    print(clf.predict(testSetX2))
    value3 = clf.score(testSetX2, testSetY2)


    print("And in fact the real values are : ")
    print(testSetY)




    '''print('Values : ')
    print(value1)
    print(value2)
    print(value3)
    '''

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
