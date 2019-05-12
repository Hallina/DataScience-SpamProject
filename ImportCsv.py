
import csv



def importcsv(pathFile):

    importation = []
    with open(pathFile, encoding='ascii', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #global importation
        for row in reader:
            importation.append(row)
        csvfile.close()

    return importation