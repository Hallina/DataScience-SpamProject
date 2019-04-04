#!/bin/python3

import csv

importation = list()


def importcsv():
    firstline = False
    with open("spambase.data", encoding='ascii', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        global importation
        for row in reader:
            importation.append(row)
        csvfile.close()


importcsv()
