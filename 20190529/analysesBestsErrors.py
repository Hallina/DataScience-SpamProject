from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import numpy as np
from sklearn import preprocessing
from importation_pandas import importcsv
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import QuantileTransformer



setX, setY = importcsv()
X, X_t, y, y_t = train_test_split(setX, setY, test_size=0.05)
scaler1 = StandardScaler()
scaler1.fit(X)
usedDataScale2 = scaler1.transform(X)
testSetXScale2 = scaler1.transform(X_t)

X_normalized = preprocessing.normalize(X, norm='l2')
X_test_normalized = preprocessing.normalize(X_t, norm='l2')

quantile_transformer = preprocessing.QuantileTransformer(output_distribution='normal', random_state=0)
X_trans = quantile_transformer.fit_transform(X)
X_test_trans = quantile_transformer.fit_transform(X_t)

max_iter = 300
param = {'solver': 'adam', 'learning_rate_init': 0.01}


'''listClassifier = [ExtraTreesClassifier(n_estimators=50), AdaBoostClassifier(n_estimators=200), MLPClassifier(verbose=0, random_state=0,max_iter=max_iter, **param), SVC(kernel="linear", C=0.2)]
listNameClassifier = ["Extra tree", "Adaboost", "MLPClass", "SVC"]
'''
listClassifier = [ExtraTreesClassifier(n_estimators=50), AdaBoostClassifier(n_estimators=200), MLPClassifier(verbose=0, random_state=0,max_iter=max_iter, **param)]
listNameClassifier = ["Extra tree", "Adaboost", "MLP"]

pred = {"Extra tree": [], "Adaboost": [], "MLP":[]}
predProba = {"Extra tree": [], "Adaboost": [], "MLP":[]}



for k in range(len(listClassifier)):
    #print(listNameClassifier[k])
    clf = listClassifier[k]
    if listNameClassifier[k] in ["Adaboost", "SVC"]:
        X_train = X_normalized
        X_test = X_test_normalized
    else:
        X_train = X_trans
        X_test = X_test_trans

    clf = clf.fit(X_train, y)
    #print(clf.feature_importances_)

    model = SelectFromModel(clf, prefit=True)
    #X_new = model.transform(X)
    #X_new.shape

    #print(clf.score(X_test, y_t))
    #pred = clf.predict(X_test)
    #print(confusion_matrix(y_t,pred))
    #print(pred)
    #print(clf.predict_proba(X_test))
    print(listNameClassifier[k])
    pred[listNameClassifier[k]] = clf.predict(X_test)
    predProba[listNameClassifier[k]] = clf.predict_proba(X_test)


#print(y_t)

definiteAnswers = []
choice = []


for nbAnswer in range(len(pred["Adaboost"])):
    if max(predProba["Adaboost"][nbAnswer]) > 0.55:
        definiteAnswers.append(pred["Adaboost"][nbAnswer])
        choice.append(0)
    else:
        '''if max(predProba["Extra tree"][nbAnswer]) == 1 and pred["Adaboost"][nbAnswer] == pred["Extra tree"][nbAnswer]:
            definiteAnswers.append(pred["Adaboost"][nbAnswer])
            choice.append(1)
        else:
            if pred["Adaboost"][nbAnswer] + pred["MLP"][nbAnswer] + pred["Extra tree"][nbAnswer] == 3 and max(predProba["Adaboost"][nbAnswer]>=0.515):
                definiteAnswers.append(1)
                choice.append(2)
            elif pred["Adaboost"][nbAnswer] + pred["MLP"][nbAnswer] + pred["Extra tree"][nbAnswer] == 0 and max(predProba["Adaboost"][nbAnswer]>=0.515):
                definiteAnswers.append(0)
                choice.append(3)

            else:
                definiteAnswers.append("")
                choice.append(4)
        '''
        definiteAnswers.append(pred["Extra tree"][nbAnswer])
        choice.append(1)



nbOk = 0
nbNoChoiceOK = 0
nbSuppr = 0
answersChoice = {0:0, 1:0, 2:0, 3:0}


for nbAnswer in range(len(definiteAnswers)):
    if definiteAnswers[nbAnswer] != "":
        if definiteAnswers[nbAnswer] == y_t[nbAnswer]:
            nbOk +=1

        else:
            print(nbAnswer)
            #print(choice[nbAnswer])
            answersChoice[choice[nbAnswer]] += 1

    else:
        nbSuppr+=1
        if pred["Extra tree"][nbAnswer] == y_t[nbAnswer]:
            nbNoChoiceOK += 1

print((nbOk/(len(definiteAnswers)-nbSuppr))*100)
print(nbSuppr)
print(definiteAnswers)
print(pred["Adaboost"])
print(y_t)
print(len(y_t))
print(answersChoice)

#print((nbNoChoiceOK/nbSuppr)*100)


