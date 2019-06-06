
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC

from importation_pandas import importcsv
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix


setX, setY = importcsv()
X_train, X_test, y_train, y_test = train_test_split(setX, setY, test_size=0.02)




# Training SVM and Naive bayes classifier

model1 = BernoulliNB()
model2 = LinearSVC()
model1.fit(X_train,y_train)
model2.fit(X_train,y_train)

result1 = model1.predict(X_test)
result2 = model2.predict(X_test)
print(confusion_matrix(y_test,result1))
print(confusion_matrix(y_test,result2))
print(model1.score(X_test, y_test))
print(model2.score(X_test, y_test))