#!/bin/python3

import pandas as pd
import numpy as np
from random import random


def importcsvNotAll(pathFile, ):

    importation = []
    with open(pathFile, encoding='ascii', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #global importation
        for row in reader:
            importation.append(row)
        csvfile.close()



    valspam = []
    for line in importation:
        l = line.pop(-1)
        valspam.append(l)
        for value in [31, 28, 27]:
            line.pop(value)
    other = importation.deepcopy()




    return importation






    if nameIndiceToAvoid != []:
        for indice in nameIndiceToAvoid:
            other.pop(indice)


    if nameIndiceToTake != "All":
        for indice in t:
            if indice not in nameIndiceToTake:
                other.pop(indice)

    t = []
    k = []
    answers = []


    for l in read:
        list = []
        for line in read[l]:
            list.append(line)
        t.append(list)

    for l in other:
        list = []
        for line in other[l]:
            list.append(line)
        #print(list)
        k.append(list)

    #print(valspam)
    for l in valspam:
        answers.append(l)


    #print(answers)



    # shuffle du dataset de base
    #t.reindex(np.random.permutation(t.index))

    #on récupère la variable isSpam





    testSetX = []
    testSetY = []
    testSetX1 = []
    print(len(k))
    for r in range(int(percentElementTest*len(k))):
        placeToTakeForTest = int(random() * len(k))
        #print(t)
        x = t.pop(placeToTakeForTest)
        y = valspam.pop(placeToTakeForTest)
        #print(x)
        testSetX.append(x)
        testSetY.append(y)
        x1 = k.pop(placeToTakeForTest)
        print(x1)
        testSetX1.append(x1)

    k = np.array(k)
    t = np.array(t)
    valspam = np.array(valspam)
    testSetX = np.array(testSetX)
    testSetY = np.array(testSetY)
    testSetX1 = np.array(testSetX1)


    print(len(k[0]))
    print(len(k))
    print(len(t[0]))
    print(len(t))
    print(len(testSetX))
    print(len(testSetX[0]))


    return (t, k, valspam, testSetX, testSetX1, testSetY)
