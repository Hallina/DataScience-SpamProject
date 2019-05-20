from sklearn.neural_network import MLPClassifier
from random import random
from ImportCsv import importcsv
import numpy as np
from analyse_stats.draw_similarities_middle import drawSimilarities as drawSimilarities1
from analyse_stats.draw_class_repartition import drawSimilarities as drawSimilarities2
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC




pathFile = "../spambase.data"
better = 0
worst = 0
nbTurns = 1
nbNeighbors=1
weightValue = "distance"
totMod1 = 0
totMod2 = 0
totNonMod = 0
precision = 0.3
valueToCompare = 0.001
nbElementTest = 1000

goodLines1 = drawSimilarities1(range(57), 2, valueToCompare, pathFile, False)
goodLines2 = drawSimilarities2(range(57), precision, valueToCompare, pathFile, False)
#print(goodLines1)
#print(goodLines2)

totGen = 0

listNbPb = []
listPb = []
listNoPb = []

clsf1 = AdaBoostClassifier(n_estimators=200)
clsf2 = MLPClassifier()
clsf3 = KNeighborsClassifier(n_neighbors=nbNeighbors, weights=weightValue)
clsf4 = tree.DecisionTreeClassifier()
clsf5 = SVC(kernel="linear", C=0.2)

tot = 0
totCancelled = 0
for tour in range(nbTurns):




    print(tour)
    # Load data
    rowData = importcsv(pathFile)
    data = []
    for line in rowData:
        listLine = []
        for value in  line:
            listLine.append(float(value))
        data.append(listLine)

    usedData = []
    usedValue = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k not in [27, 28, 31, 57, 3, 30, 32, 36, 39, 40, 46, 47]:
                listLine.append(line[k])
        usedValue.append(line[-1])
        usedData.append(listLine)
    '''data = np.array(data)
    print(data)
    '''

    usedData1 = []
    usedValue1 = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in goodLines2 and k not in [27, 28, 31, 57, 3, 30, 32, 36, 39, 40, 46, 47]:

                listLine.append(line[k])
        usedValue1.append(line[-1])
        usedData1.append(listLine)
    '''data = np.array(data)
    print(data)
    '''

    usedData3 = []
    usedValue3 = []
    for line in data:
        listLine = []
        for k in range(len(line)):
            if k in [56, 55, 54]:
                listLine.append(line[k])
        usedValue3.append(line[-1])
        usedData3.append(listLine)
    '''data = np.array(data)
    print(data)
    '''



    testSetX = []
    testSetY = []
    testSetX1 = []
    testSetY1 = []
    testSetX3 = []
    testSetY3 = []
    listPlaceToTakeForTest = []
    nbElementDeleted = 0
    for k in range (nbElementTest):
        placeToTakeForTest = int(random() * len(usedData))
        listPlaceToTakeForTest.append(placeToTakeForTest)
        x = usedData.pop(placeToTakeForTest-nbElementDeleted)
        y = usedValue.pop(placeToTakeForTest-nbElementDeleted)
        testSetX.append(x)
        testSetY.append(y)
        x1 = usedData1.pop(placeToTakeForTest-nbElementDeleted)
        y1 = usedValue1.pop(placeToTakeForTest-nbElementDeleted)
        testSetX1.append(x1)
        testSetY1.append(y1)
        x3 = usedData3.pop(placeToTakeForTest-nbElementDeleted)
        y3 = usedValue3.pop(placeToTakeForTest-nbElementDeleted)
        testSetX3.append(x3)
        testSetY3.append(y3)
        nbElementDeleted += 1






    usedData = np.array(usedData)
    usedValue = np.array(usedValue)
    testSetX = np.array(testSetX)
    testSetY = np.array(testSetY)
    usedData1 = np.array(usedData1)
    usedValue1 = np.array(usedValue1)
    testSetX1 = np.array(testSetX1)
    testSetY1 = np.array(testSetY1)

    scaler1 = StandardScaler()
    scaler1.fit(usedData)
    usedDataScale2 = scaler1.transform(usedData)
    testSetXScale2 = scaler1.transform(testSetX)

    scaler3 = StandardScaler()
    scaler3.fit(usedData3)
    usedDataScale3 = scaler3.transform(usedData3)
    testSetXScale3 = scaler3.transform(testSetX3)




    clf1 = clsf1.fit(usedDataScale2, usedValue)
    value1 = clf1.predict_proba(testSetXScale2)
    value1Pred = clf1.predict(testSetXScale2)
    value1Score = clf1.score(testSetXScale2, testSetY)



    clf2 = clsf2.fit(usedData, usedValue)
    value2 = clf2.predict_proba(testSetX)
    value2Pred = clf2.predict(testSetX)
    value2Score = clf2.score(testSetX, testSetY)

    clf3 = clsf3.fit(usedDataScale3, usedValue1)

    clf4 = clsf4.fit(usedDataScale3, usedValue)


    clf = clsf5.fit(usedDataScale2, usedValue)
    value5Score = clf.score(testSetXScale2, testSetY)
    value5 = clf.predict(testSetXScale2)






    '''print(value1Score)
    print(value2Score)
    print(value3Score)
    print(value4Score)
    '''


    result = []
    cancelled = 0
    good = 0
    for k in range(nbElementTest):
        probaAda = value1[k]
        probaNN = value2[k]
        noRisk = True


        if probaAda[0]>0.6:
            result.append(0)
        elif probaAda[1]>0.6:
            result.append(1)

        else:
            if probaNN[1]>12*probaNN[0] and probaAda[1]>0.5025:
                result.append(1)
                continue
            elif probaNN[0]>12*probaNN[1] and probaAda[0]>0.5025:
                result.append(0)
                continue

            elif probaAda[0] > 0.51 and probaNN[0]>probaNN[1]:
                result.append(0)
                continue
            elif probaAda[1] > 0.51 and probaNN[1]>probaNN[0]:
                result.append(1)
                continue




            else:



                if probaAda[0] > probaAda[1] and probaAda[1] < 0.4945:
                    answerAda = 0  # the answer is 0
                elif probaAda[1] > probaAda[0] and probaAda[0] < 0.4945:
                    answerAda = 1  # the answer is 1
                else:
                    answerAda = -1


                if probaNN[0]>probaNN[1]*30 :
                    answerNN = 0# the answer is 0
                elif probaNN[1]>probaNN[0]*30:
                    answerNN = 1# the answer is 1
                else:
                    answerNN = -1 #-1 meaning no definite answer


                if answerAda == answerNN and answerAda != -1:
                    #all agrees
                    result.append(answerAda)
                else :
                    result.append(-1)
                    cancelled += 1
                    continue



                    '''elif answerAda == -1 and answerNN != -1:
                        # disagrees
                        result.append(-1)
                        noRisk = False
                        values = [probaAda, probaNN]
                        #result.append(answerNN)
                    elif answerNN == -1 and answerAda != -1:
                        result.append(-1)
                        noRisk = False
                        values = [probaAda, probaNN]
                        #result.append(answerAda)
                    '''
                #else:
                    value3 = clf3.predict([testSetXScale3[k]])
                    value4 = clf4.predict([testSetXScale3[k]])
                    '''print("erreur?")
                    print(answerAda, answerNN, value3, value4)
                    print(testSetY[k])
                    '''
                    if value4 == value3:
                        result.append(int(value4[0]))
                        #result.append(-1)
                    else:
                        result.append(-1)

            '''if not noRisk:
                print('here')
                print(values)
                print([answerAda, answerNN])
                value3 = clf3.predict([testSetXScale3[k]])
                value4 = clf4.predict([testSetXScale3[k]])
                print(value3)
                print(value4)
                print(testSetY[k])'''


        if result[-1] == -1:
            listPb.append(usedData[k])
            cancelled += 1
        else:
            listNoPb.append(usedData[k])



    #print("Au final : ")
    print(value1)
    print(value2)
    print(value1Pred)
    print(value2Pred)
    print(value5)
    print(result)
    print(testSetY)

    good = 0
    for lk in range(len(result)):
        if result[lk]!=-1 and int(testSetY[lk]) == int(result[lk]):
            good+=1
        elif result[lk]!=-1 and int(testSetY[lk]) != int(result[lk]):
            listNbPb.append(listPlaceToTakeForTest[lk])




    currentResult = (good/(len(result)-cancelled))*100
    tot += currentResult
    totCancelled += cancelled
    print(cancelled)
    print(currentResult)

print(tot/nbTurns)
print("Cancelled : ")
print(totCancelled)

#print(listPb)

'''dicoPb = {}
for k in range(len(listPb[0])):
    dicoPb[k] = 0

for k in range(len(listPb)):
    for j in range(len(listPb[k])):
        dicoPb[j] += listPb[k][j]/len(listPb)




dicoNoPb = {}
for k in range(len(listNoPb[0])):
    dicoNoPb[k] = 0

for k in range(len(listNoPb)):
    for j in range(len(listNoPb[k])):
        dicoNoPb[j] += listNoPb[k][j]/len(listNoPb)
        
'''


'''for k in range(len(listNoPb[0])):
    print(str(k) + " : ")
    print(dicoPb[k])
    print(dicoNoPb[k])
'''

print('errors : ')
print(listNbPb)
'''print(listPlaceToTakeForTest)
print(result)
print(testSetY)
'''







