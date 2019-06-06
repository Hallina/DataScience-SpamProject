from importation_pandas import importcsv

import numpy as np
import matplotlib.pyplot as plt
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

from sklearn.model_selection import train_test_split

names = ["Nearest Neighbors", "RBF SVM", #"Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(gamma=2, C=1),
    #GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1, max_iter=1000),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

val, valspam = importcsv()

train, test = train_test_split(val, test_size=0.5)
spamtrain, spamtest = train_test_split(valspam, test_size=0.5)

scores = list()

# iterate over classifiers
for name, clf in zip(names, classifiers):
    clf.fit(train, spamtrain)
    score = clf.score(test, spamtest)
    print(name)
    print(score)
    scores.append(score)


#ajout plot

fig, ax = plt.subplots()

ind = np.arange(len(scores))
width = 0.35

rects1 = ax.bar(ind - width/2, scores, width)

ax.set_ylabel('Scores')
ax.set_title('Classicals scores by classifiers')
ax.set_xticks(ind)
ax.set_xticklabels(names, rotation=40, ha='right')
vals = ax.get_yticks()
ax.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
ax.legend()

fig.tight_layout()

plt.show()
