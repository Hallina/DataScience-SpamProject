from sklearn import tree
from random import random
from importation import importcsv
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

listErrorsToStudy = [1783, 1719, 3332, 4366, 2197, 1727, 2362, 1823, 2346, 1297, 1715, 4295, 2380, 896, 4333, 374, 1484, 3814, 2466, 189, 4127, 686, 3056, 1605, 4365, 1795, 1637, 381, 3824, 845, 1838, 274, 2394, 2939, 305, 3889, 1675, 2552, 263, 1799, 2951, 3947, 4137, 1173, 1015, 294, 3460, 2075, 3546, 2219, 2042, 2157, 1811, 1590, 3490, 3926, 2136, 3243, 1228, 2885]

dicoResults = {}

classifiers = [
    AdaBoostClassifier(n_estimators = 200),
    MLPClassifier(),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    KNeighborsClassifier(n_neighbors = 2, weights = "distance"),
    SVC(gamma=2, C=1)
    ]

names = ["AdaBoost", "Neural Net", "Decision Tree", "Random Forest",  "Nearest Neighbors","RBF SVM"]

rowData = importcsv("spambase.data")
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
        #if k not in [27, 28, 31, 57, 0,3,14,16,22,24,26,30,31, 32, 33, 34, 37, 39, 40, 41,42,  46,47, 50, 51]: 0,3,14,16,22,24,26,30,31, 32, 33, 34, 37, 39, 40, 41,42,  46,47, 50, 51
        if k not in [27, 28, 31, 57 ]:
            listLine.append(line[k])
    usedValue.append(line[-1])
    usedData.append(listLine)


testSetX = []
testSetY = []
for placeToTakeForTest in listErrorsToStudy:
    x = usedData.pop(placeToTakeForTest)
    y = usedValue.pop(placeToTakeForTest)
    testSetX.append(x)
    testSetY.append(y)

scaler = StandardScaler()
usedData = np.array(usedData)
usedValue = np.array(usedValue)
testSetX = np.array(testSetX)
testSetY = np.array(testSetY)
scaler.fit(usedData)
usedDataScale = scaler.transform(usedData)
testSetXScale = scaler.transform(testSetX)



print(testSetY)
for nbClassifiers in range(len(classifiers)):
    print(names[nbClassifiers])

    clf = classifiers[nbClassifiers]
    clf = clf.fit(usedData, usedValue)

    a = clf.predict(testSetX)
    #print(a)
    #print(testSetY)


    print(clf.score(testSetX, testSetY))
    dicoResults[nbClassifiers] = a



