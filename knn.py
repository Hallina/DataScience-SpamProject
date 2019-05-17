import importation

from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn import preprocessing
from sklearn.decomposition import PCA

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as plt

train, test = train_test_split(importation.t, test_size=0.05)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.05)

clf = make_pipeline(preprocessing.StandardScaler(),
                    PCA(n_components=2),
                    KNeighborsClassifier(n_neighbors=5,
                                         weights="uniform",
                                         algorithm="auto",
                                         n_jobs=4)
                    )

clf.fit(train, spamtrain)

expected = spamtest
predicted = clf.predict(test)

print(clf.score(train, spamtrain))
print(clf.score(test, spamtest))

print("Classification report for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


