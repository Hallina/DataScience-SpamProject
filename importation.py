#!/bin/python3

import pandas as pd
import csv
importation = list()

t = pd.read_csv("spambase.data", names=['word_freq_make'
                ,'word_freq_address'
                ,'word_freq_all'
                ,'word_freq_3d'
                ,'word_freq_our'
                ,'word_freq_over'
                ,'word_freq_remove'
                ,'word_freq_internet'
                ,'word_freq_order'
                ,'word_freq_mail'
                ,'word_freq_receive'
                ,'word_freq_will'
                ,'word_freq_people'
                ,'word_freq_report'
                ,'word_freq_addresses'
                ,'word_freq_free'
                ,'word_freq_business'
                ,'word_freq_email'
                ,'word_freq_you'
                ,'word_freq_credit'
                ,'word_freq_your'
                ,'word_freq_font'
                ,'word_freq_000'
                ,'word_freq_money'
                ,'word_freq_hp'
                ,'word_freq_hpl'
                ,'word_freq_george'
                ,'word_freq_650'
                ,'word_freq_lab'
                ,'word_freq_labs'
                ,'word_freq_telnet'
                ,'word_freq_857'
                ,'word_freq_data'
                ,'word_freq_415'
                ,'word_freq_85'
                ,'word_freq_technology'
                ,'word_freq_1999'
                ,'word_freq_parts'
                ,'word_freq_pm'
                ,'word_freq_direct'
                ,'word_freq_cs'
                ,'word_freq_meeting'
                ,'word_freq_original'
                ,'word_freq_project'
                ,'word_freq_re'
                ,'word_freq_edu'
                ,'word_freq_table'
                ,'word_freq_conference'
                ,'char_freq_;'
                ,'char_freq_('
                ,'char_freq_['
                ,'char_freq_!'
                ,'char_freq_$'
                ,'char_freq_#'
                ,'capital_run_length_average'
                ,'capital_run_length_longest'
                ,'capital_run_length_total'
                ,'isSpam'])



#on récupère la variable isSpam
valspam = t.pop('isSpam').values

<<<<<<< HEAD
def importcsv():
    firstline = False
    with open("spambase.data", encoding='ascii', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        global importation
        for row in reader:
            importation.append(row)
        csvfile.close()

    return importation




data = importcsv()
#print(data[0:10])
=======
onflit.pop('word_freq_650')
t.pop('word_freq_george')
