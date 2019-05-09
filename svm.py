import importation

from sklearn.linear_model import BayesianRidge, LinearRegression

from sklearn import svm
from sklearn import metrics

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

train, test = train_test_split(importation.t, test_size=0.2)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.2)


clf = BayesianRidge(compute_score=True)
ols = LinearRegression()

clf.fit(train, spamtrain)
ols.fit(train, spamtrain)

expected = spamtest
predicted = clf.predict(test)

predicted1 = ols.predict(test)

"""
print("Classification report for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
"""

lw = 2

plt.figure(figsize=(6, 5))
plt.title("Weights of the model")
plt.plot(clf.coef_, color='lightgreen', linewidth=lw,
         label="Bayesian Ridge estimate")
plt.plot(ols.coef_, color='navy', linestyle='--', label="OLS estimate")
plt.xlabel("Features")
plt.ylabel("Values of the weights")
plt.legend(loc="best", prop=dict(size=12))

plt.show()
