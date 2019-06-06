from sklearn.kernel_ridge import KernelRidge
import numpy as np

from importation_pandas import importcsv
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix



setX, setY = importcsv()
X_train, X_test, y_train, y_test = train_test_split(setX, setY, test_size=0.3)


clf = KernelRidge(alpha=1.0)
clf.fit(X_train, y_train)
result1 = clf.predict(X_test)
print(clf.score(X_test, y_test))
print(confusion_matrix(y_test,result1))