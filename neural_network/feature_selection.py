



from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities as drawSimilarities1
from analyse_stats.draw_class_repartition import drawSimilarities as drawSimilarities2
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import LinearSVC
from sklearn.ensemble import ExtraTreesClassifier


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

#lsvc = MLPClassifier().fit(usedData, usedValue)
lsvc = LinearSVC().fit(usedData, usedValue)
#print(usedData[0])
print(lsvc.score(testSetX, testSetY))
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(usedData)
X_test_new = model.transform(testSetX)
#X_new.shape
#print(X_new[0])
clf = LinearSVC().fit(X_new, usedValue)
print(clf.score(X_test_new, testSetY))





clf = ExtraTreesClassifier()
clf = clf.fit(usedData,usedValue )
print(clf.score(testSetX, testSetY))
print(clf.feature_importances_)
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(usedData)
X_new.shape
X_new_test = model.transform(testSetX)
X_new_test.shape

clf = clf.fit(X_new,usedValue )
print(clf.score(X_new_test, testSetY))




