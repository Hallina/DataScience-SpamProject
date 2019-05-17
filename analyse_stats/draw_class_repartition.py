import ImportCsv
import matplotlib.pyplot as plt


#
#
# plt.title('Error Rate K Value')
# plt.xlabel('K Value')
# plt.ylabel('Mean Error')


def drawSimilarities(listPlaceOfWordToCompare, precision, valueToCompare, pathFile, draw = True):
    nbOk = []
    file = ImportCsv.importcsv(pathFile)
    for placeOfWordToCompare in listPlaceOfWordToCompare:
        #print("place of word : ")
        #print(placeOfWordToCompare)
        if draw :
            plt.figure()
            plt.title('Word nb = ' + str(placeOfWordToCompare))

        k = 0
        spamClasses = {"<value": [], "value<": []}
        nonSpamClasses = {"<value": [], "value<": []}

        totSpam = 0
        totNonSpam = 0

        for line in file:
            value = float(line[placeOfWordToCompare])
            if value < valueToCompare:
                if int(line[-1]) == 1:
                    spamClasses["<value"].append(value)
                    totSpam += 1
                else:
                    nonSpamClasses["<value"].append(value)
                    totNonSpam += 1
            else:
                if int(line[-1]) == 1:
                    spamClasses["value<"].append(value)
                    totSpam += 1
                else:
                    nonSpamClasses["value<"].append(value)
                    totNonSpam += 1

        results = []
        nbPlot = 1
        for type in [spamClasses, nonSpamClasses]:
            try :
                totalType = len(type["value<"]) + len(type["<value"])
                totalInf = len(type["<value"])/totalType
                totalSup = len(type["value<"])/totalType
            except:
                totalInf, totalSup, totalNonSpam = 0,0,0

            results.append(totalInf)
            results.append(totalSup)
            if draw:
                labels = "value<", "value >"
                sizes = [totalInf, totalSup]
                colors = ['yellowgreen', 'lightskyblue']
                plt.subplot(210+nbPlot)
                nbPlot+=1
                plt.title("For : " + " : " + str(valueToCompare) + " for the word nb : " + str(placeOfWordToCompare) + " with a number of " + str(totalType) + " emails concerned")
                plt.pie(sizes, labels=labels, colors=colors,
                        autopct='%1.1f%%', shadow=True, startangle=90)

        print(results)
        if (abs(results[0] - results[2]) > precision) :

            #print("okk")
            nbOk.append(placeOfWordToCompare)
            if draw :
                plt.axis('equal')
                plt.savefig('PieChart01.png')
                plt.show()

        else:
            if draw:
                plt.close()


    return nbOk
'''
val = {}
for k in [0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 3]:
    val[k] = len(drawSimilarities(range(57), 0.3, k, "../spambase.data", False))

print(val)
#'''


#print(drawSimilarities(range(57), 0.4, 0.001, "../spambase.data"))

'''

import matplotlib.pyplot as plt

labels = 'Allemagne', 'France', 'Belgique', 'Espagne'
sizes = [15, 80, 45, 40]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.savefig('PieChart01.png')
plt.show()

[11, 6, 10, 5, 8, 15]
'''