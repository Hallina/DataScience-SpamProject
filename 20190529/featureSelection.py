from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split

from importation_pandas import importcsv

from sklearn.metrics import confusion_matrix



setX, setY = importcsv()
X, X_test, y, y_test = train_test_split(setX, setY, test_size=0.3)


clf = ExtraTreesClassifier(n_estimators=50)
clf = clf.fit(X, y)
print(clf.feature_importances_)

model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
#X_new.shape

print(clf.score(X_test, y_test))
pred = clf.predict(X_test)
print(confusion_matrix(y_test,pred))