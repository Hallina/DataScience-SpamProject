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

dicoResults = {}

classifiers = [
    AdaBoostClassifier(n_estimators = 200),
    SVC(kernel="linear", C=0.025),
    MLPClassifier(),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    KNeighborsClassifier(n_neighbors = 2, weights = "distance"),

    #GaussianProcessClassifier(1.0 * RBF(1.0)),



    #GaussianNB(),
    SVC(gamma=2, C=1)
    #QuadraticDiscriminantAnalysis(),
    ]

names = ["AdaBoost", "Linear SVM", "Neural Net", "Decision Tree", "Random Forest",  "Nearest Neighbors",
          "RBF SVM"
         ]#"QDA",#"Gaussian Process","Naive Bayes"

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
        if k not in [27, 28, 31, 57, 0,3,14,16,22,24,26,30,31, 32, 33, 34, 37, 39, 40, 41,42,  46,47, 50, 51]:
            listLine.append(line[k])
    usedValue.append(line[-1])
    usedData.append(listLine)


testSetX = []
testSetY = []
for k in range(24):
    placeToTakeForTest = int(random() * len(usedData))
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
usedValueScale = scaler.transform(usedValue)



print(testSetY)
for nbClassifiers in range(len(classifiers)):

    #print(names[nbClassifiers])

    # Load data

    '''data = np.array(data)
    print(data)
    '''




    #print(usedData[:1])
    clf = classifiers[nbClassifiers]
    clf = clf.fit(usedData, usedValue)


    a = clf.predict(testSetX)
    print(a)
    #print(testSetY)


    #print(clf.score(testSetX, testSetY))
    dicoResults[nbClassifiers] = a

'''

result = []
for key in dicoResults:
    print(dicoResults[key])
for line in range(len(testSetY)):
    value = 0
    for key in dicoResults:
        value+=dicoResults[key][line]

    if value >= 3:
        result.append(1)
    else:
        result.append(0)

goodChoices = 0
for k in range(len(result)):
    if result[k] == testSetY[k]:
        goodChoices+=1

print("Au final : ")
print(goodChoices/len(result))

print(result)
print(testSetY)
'''


