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



classifiers = [
    KNeighborsClassifier(3),
    SVC(gamma=2, C=1),
    #GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]
    #SVC(kernel="linear", C=0.025)]

names = ["Nearest Neighbors",  "RBF SVM", #"Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"] #"Linear SVM"]


for nbClassifiers in range(len(classifiers)):

    print(names[nbClassifiers])

    # Load data
    rowData = importcsv()
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
            if k != 27 and k != 28 and k != 32 and k!=57:
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

    #print(usedData[:1])
    clf = classifiers[nbClassifiers]
    clf = clf.fit(usedData, usedValue)


    a = clf.predict(testSetX)
    #print(a)
    #print(testSetY)

    good = 0
    bad = 0
    for k in range(len(a)):
        if a[k] == testSetY[k]:
            good+=1
        else:
            bad+=1



    print((good/(good+bad))*100)
    print((bad/(good+bad))*100)
    print('Score : ')
    print(clf.score(usedData, usedValue))