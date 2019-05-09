import importation

from sklearn import svm
from sklearn import metrics

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

train, test = train_test_split(importation.t, test_size=0.5)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.5)


clf = svm.SVC(gamma='scale')

clf.fit(train, spamtrain)

expected = spamtest
predicted = clf.predict(test)

print(clf.score(train, spamtrain))

print("Classification report for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


