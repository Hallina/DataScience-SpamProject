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
        for type in ["<value", "value<"]:
            try :
                totalType = len(spamClasses[type]) + len(nonSpamClasses[type])
                totalSpam = len(spamClasses[type])/totalType
                totalNonSpam = len(nonSpamClasses[type])/totalType
            except:
                totalType, totalSpam, totalNonSpam = 0,0,0

            results.append(totalSpam)
            results.append(totalNonSpam)
            if draw:
                labels = "Spam", "Non Spam"
                sizes = [totalSpam, totalNonSpam]
                colors = ['yellowgreen', 'lightskyblue']
                plt.subplot(210+nbPlot)
                nbPlot+=1
                plt.title("For : " + str(type) + " : " + str(valueToCompare) + " for the word nb : " + str(placeOfWordToCompare) + " with a number of " + str(totalType) + " emails concerned")
                plt.pie(sizes, labels=labels, colors=colors,
                        autopct='%1.1f%%', shadow=True, startangle=90)

        if (results[0]*100 > results[1]*100*precision or results[1]*100 > results[0]*100*precision):
            if (results[2] * 100 > results[3] * 100 * precision or results[3] *100 > results[2] * 100 *precision):
                #print("okk")
                nbOk.append(placeOfWordToCompare)
                if draw :
                    plt.axis('equal')
                    plt.savefig('PieChart01.png')
                    plt.show()
            else:
                if draw:
                    plt.close()
        else:
            if draw:
                plt.close()


    return nbOk


#print(drawSimilarities(range(57), 1.5, 0.2, "../spambase.data"))

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