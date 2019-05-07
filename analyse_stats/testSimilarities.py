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
    for line in file:
        value= float(line[placeOfWordToCompare])*100
        #print(value)
        if int(line[-1])==1:
            color = 'blue'
            if value<200:
                plt.plot(value , value+10, color=color, linestyle='dashed', marker='o',markerfacecolor=color, markersize=3)
        else:
            color = 'orange'
            if value<200:
                plt.plot(value, value-10, color=color, linestyle='dashed', marker='o',markerfacecolor=color, markersize=3)

        k+=1
    print('rrrr')
    plt.show()

drawSimilarities(15)
print('kjkjk')

