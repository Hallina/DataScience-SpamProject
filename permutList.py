from random import random


def permutList(list1, list2):

    newList1 = []
    newList2 = []
    nbTurn  = len(list1)

    for k in range(nbTurn):
        x = int(random()*len(list1))
        value1 = list1.pop(x)
        newList1.append(value1)
        value2 = list2.pop(x)
        newList2.append(value2)


    return newList1, newList2



