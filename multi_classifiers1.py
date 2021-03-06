from sklearn import tree
from random import random
import importation
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

train, test = train_test_split(importation.t, test_size=0.05)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.05)

expected = spamtest

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
         "Naive Bayes", "QDA"]#, "Linear SVM"]


for nbClassifiers in range(len(classifiers)):

    print(names[nbClassifiers])

    #load data

    
    clf = classifiers[nbClassifiers]
    clf.fit(train, spamtrain)


    predicted = clf.predict(test)
    
    print(clf.score(train, spamtrain))
    print(clf.score(test, spamtest))
