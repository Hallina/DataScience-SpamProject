from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron

from importation_pandas import importcsv
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix


setX, setY = importcsv()
X_train, X_test, y_train, y_test = train_test_split(setX, setY, test_size=0.3)

for k in range(0,10,1):
    alpha = 0.0001*(10**k)
    clf = Perceptron(tol=1e-3, random_state=0, class_weight=None)
    clf.fit(X_train, y_train)


    result1 = clf.predict(X_test)

    print(alpha)

    print(clf.score(X_test, y_test))

    print(confusion_matrix(y_test,result1))
