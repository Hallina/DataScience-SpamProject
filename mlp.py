import importation

from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn import preprocessing

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as plt

train, test = train_test_split(importation.t, test_size=0.05)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.05)

clf = MLPClassifier(alpha=1,
                    activation='relu',
                    solver='adam',
                    learning_rate='constant',
                    verbose=True)

clf.fit(train, spamtrain)

expected = spamtest
predicted = clf.predict(test)

print(clf.score(train, spamtrain))
print(clf.score(test, spamtest))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


