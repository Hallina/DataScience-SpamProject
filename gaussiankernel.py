import importation


from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF, DotProduct

from sklearn import metrics

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

train, test = train_test_split(importation.t, test_size=0.1)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.1)

kernels = [1.0 * RBF(length_scale=1.0), 1.0 * DotProduct(sigma_0=1.0)**2]

for i, kernel in enumerate(kernels):
    clf = GaussianProcessClassifier(kernel=kernel, warm_start=True)

    clf.fit(train, spamtrain)

    expected = spamtest
    predicted = clf.predict(test)

    print(clf.score(train, spamtrain))

    print("Classification report for classifier %s:\n%s\n"
          % (clf, metrics.classification_report(expected, predicted)))

    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

    print("LA SUITE...\n\n\n\n")
