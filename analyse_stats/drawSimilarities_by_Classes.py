import importation
import matplotlib.pyplot as plt


#
#
# plt.title('Error Rate K Value')
# plt.xlabel('K Value')
# plt.ylabel('Mean Error')


def drawSimilarities(placeOfWordToCompare):

    plt.figure()
    file = importation.importcsv()
    k=0
    spamClasses = {"<0.05": [], "0.05<0.5": [], "0.5<1": [], "1<1.5": [], "1.5<2": [], "2<": []}
    nonSpamClasses = {"<0.05": [], "0.05<0.5": [], "0.5<1": [], "1<1.5": [], "1.5<2": [], "2<": []}

    totSpam = 0
    totNonSpam = 0

    for line in file:
        value= float(line[placeOfWordToCompare])
        if value<0.05:
            if int(line[-1]) == 1:
                spamClasses["<0.05"].append(value)
                totSpam+=1
            else:
                nonSpamClasses["<0.05"].append(value)
                totNonSpam+=1
        elif 0.05<=value and value<0.5:
            if int(line[-1]) == 1:
                spamClasses["0.05<0.5"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["0.05<0.5"].append(value)
                totNonSpam += 1
        elif 0.5<=value and value<1:
            if int(line[-1]) == 1:
                spamClasses["0.5<1"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["0.5<1"].append(value)
                totNonSpam += 1

        elif 1<=value and value<1.5:
            if int(line[-1]) == 1:
                spamClasses["1<1.5"].append(value)
                totSpam+=1
            else:
                nonSpamClasses["1<1.5"].append(value)
                totNonSpam += 1

        elif 1.5<=value and value<2:
            if int(line[-1]) == 1:
                spamClasses["1.5<2"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["1.5<2"].append(value)
                totNonSpam += 1

        elif 2<=value:
            if int(line[-1]) == 1:
                spamClasses["2<"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["2<"].append(value)
                totNonSpam += 1




    nb = 0
    for value in spamClasses:
        tot = (len(spamClasses[value])/totSpam) * 100
        plt.plot(nb, tot, color='blue', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=5)
        nb +=1
        print("\n")
        print(value)
        print(tot)
        print(totSpam)
    nb = 0
    print("\n non spam : \n")
    for value in nonSpamClasses:
        tot = (len(nonSpamClasses[value])/totNonSpam)*100
        plt.plot(nb, tot, color='orange', linestyle='dashed', marker='o', markerfacecolor='orange', markersize=5)
        nb +=1
        print("\n")
        print(value)
        print(tot)
        print(totNonSpam)

    print('rrrr')
    plt.show()



def drawSimilarities(listOfPlace):

    plt.figure()
    file = importation.importcsv()
    k=0


    totSpam = 0
    totNonSpam = 0

    for line in file:
        





        value= float(line[placeOfWordToCompare])
        if value<0.05:
            if int(line[-1]) == 1:
                spamClasses["<0.05"].append(value)
                totSpam+=1
            else:
                nonSpamClasses["<0.05"].append(value)
                totNonSpam+=1
        elif 0.05<=value and value<0.5:
            if int(line[-1]) == 1:
                spamClasses["0.05<0.5"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["0.05<0.5"].append(value)
                totNonSpam += 1
        elif 0.5<=value and value<1:
            if int(line[-1]) == 1:
                spamClasses["0.5<1"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["0.5<1"].append(value)
                totNonSpam += 1

        elif 1<=value and value<1.5:
            if int(line[-1]) == 1:
                spamClasses["1<1.5"].append(value)
                totSpam+=1
            else:
                nonSpamClasses["1<1.5"].append(value)
                totNonSpam += 1

        elif 1.5<=value and value<2:
            if int(line[-1]) == 1:
                spamClasses["1.5<2"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["1.5<2"].append(value)
                totNonSpam += 1

        elif 2<=value:
            if int(line[-1]) == 1:
                spamClasses["2<"].append(value)
                totSpam += 1
            else:
                nonSpamClasses["2<"].append(value)
                totNonSpam += 1




    nb = 0
    for value in spamClasses:
        tot = (len(spamClasses[value])/totSpam) * 100
        plt.plot(nb, tot, color='blue', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=5)
        nb +=1
        print("\n")
        print(value)
        print(tot)
        print(totSpam)
    nb = 0
    print("\n non spam : \n")
    for value in nonSpamClasses:
        tot = (len(nonSpamClasses[value])/totNonSpam)*100
        plt.plot(nb, tot, color='orange', linestyle='dashed', marker='o', markerfacecolor='orange', markersize=5)
        nb +=1
        print("\n")
        print(value)
        print(tot)
        print(totNonSpam)

    print('rrrr')
    plt.show()


for k in range(11, 16):
    drawSimilarities(k)



[11, 6, 10, 5, 8, 15]