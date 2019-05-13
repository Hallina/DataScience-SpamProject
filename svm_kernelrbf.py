import importation

from sklearn import svm
from sklearn import metrics

from sklearn.model_selection import train_test_split


train, test = train_test_split(importation.t, test_size=0.1)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.1)


clf = svm.SVC(gamma=80, cache_size=500, kernel="rbf")

clf.fit(train, spamtrain)

expected = spamtest
predicted = clf.predict(test)

print(clf.score(test, spamtest))

print("Classification report for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
