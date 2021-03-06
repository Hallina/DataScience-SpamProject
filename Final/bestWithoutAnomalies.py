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
from permutList import permutList

from importation_pandas_noShuffle import importcsv
from anomalies import find_anomalies


from sklearn.metrics import confusion_matrix

resultBest = 0
resultOthers = 0
nbTurns = 1




for kll in range(nbTurns):
    print(kll)
    setX, setY = importcsv()
    X = setX.values.tolist()
    y = setY.tolist()
    nbOfAnomalies = find_anomalies("Local Outlier Factor")


    nbAnomalyDelete = 0
    for anomalyFound in nbOfAnomalies:
        X.pop(anomalyFound-nbAnomalyDelete)
        y.pop(anomalyFound-nbAnomalyDelete)
        nbAnomalyDelete+=1

    X, y = permutList(X, y)

    X, X_t, y, y_t = train_test_split(X, y, test_size=0.05)
    scaler1 = StandardScaler()
    scaler1.fit(X)
    usedDataScale2 = scaler1.transform(X)
    testSetXScale2 = scaler1.transform(X_t)


    max_iter = 300
    param = {'solver': 'adam', 'learning_rate_init': 0.01}


    '''listClassifier = [ExtraTreesClassifier(n_estimators=50), AdaBoostClassifier(n_estimators=200), MLPClassifier(verbose=0, random_state=0,max_iter=max_iter, **param), SVC(kernel="linear", C=0.2)]
    listNameClassifier = ["Extra tree", "Adaboost", "MLPClass", "SVC"]
    '''
    listClassifier = [ExtraTreesClassifier(n_estimators=50), AdaBoostClassifier(n_estimators=200), MLPClassifier(verbose=0, random_state=0,max_iter=max_iter, **param)]
    listNameClassifier = ["Extra tree", "Adaboost", "MLP"]

    pred = {"Extra tree": [], "Adaboost": [], "MLP":[]}
    predProba = {"Extra tree": [], "Adaboost": [], "MLP":[]}


    #print("taille echantillon")
    #print(len(X))

    for k in range(len(listClassifier)):
        #print(listNameClassifier[k])
        clf = listClassifier[k]
        if listNameClassifier[k] in ["Adaboost", "SVC"]:
            X_train = usedDataScale2
            X_test = testSetXScale2
        else:
            X_train = X
            X_test = X_t

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
        #print(listNameClassifier[k])
        pred[listNameClassifier[k]] = clf.predict(X_test)
        predProba[listNameClassifier[k]] = clf.predict_proba(X_test)


        #print("resultats " + str(listNameClassifier[k]))
        #print(clf.score(X_test, y_t))


    #print(y_t)

    definiteAnswers = []
    choice = []


    for nbAnswer in range(len(pred["Adaboost"])):
        if max(predProba["Adaboost"][nbAnswer]) > 0.55:
            definiteAnswers.append(pred["Adaboost"][nbAnswer])
            choice.append(0)
        else:
            if max(predProba["Extra tree"][nbAnswer]) == 1 and pred["Adaboost"][nbAnswer] == pred["Extra tree"][nbAnswer]:
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


    nbOk = 0
    nbNoChoiceOK = 0
    nbSuppr = 0
    answersChoice = {0:0, 1:0, 2:0, 3:0}


    for nbAnswer in range(len(definiteAnswers)):
        if definiteAnswers[nbAnswer] != "":
            if definiteAnswers[nbAnswer] == y_t[nbAnswer]:
                nbOk +=1

            else:
                #print(nbAnswer)
                #print(choice[nbAnswer])
                answersChoice[choice[nbAnswer]] += 1

        else:
            nbSuppr+=1
            if pred["Extra tree"][nbAnswer] == y_t[nbAnswer]:
                nbNoChoiceOK += 1

    resultBest += (nbOk/(len(definiteAnswers)-nbSuppr))*100
    resultOthers += (nbNoChoiceOK/nbSuppr)*100


print("results of the one we are sure")
print(resultBest/nbTurns)
print("result for the other ones")
print(resultOthers/nbTurns)


