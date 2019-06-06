from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.datasets import make_regression
from importation_pandas import importcsv
from sklearn.model_selection import train_test_split


setX, setY = importcsv()
X_train, X_test, y_train, y_test = train_test_split(setX, setY, test_size=0.01, random_state=42)

regr = PassiveAggressiveRegressor(max_iter=100, random_state=0,tol=1e-3)
regr.fit(X_train, y_train)

#PassiveAggressiveRegressor(C=1.0, average=False, early_stopping=False,epsilon=0.1, fit_intercept=True, loss='epsilon_insensitive', max_iter=100, n_iter_no_change=5, random_state=0,shuffle=True, tol=0.001, validation_fraction=0.1,verbose=0, warm_start=False)


print(regr.score(X_test, y_test))

regr.densify()
pred = regr.predict(X_test)


result=[]

for k in range(len(pred)):
    if pred[k]<0.1:
        value = 0
    else:
        value =1
    if value == y_test[k]:
        result.append('O')
    else:
        result.append('X')

print(pred)
print(y_test)
print(result)


