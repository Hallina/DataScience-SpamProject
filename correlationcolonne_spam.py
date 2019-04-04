#!/bin/python3

import importation

importation.v = importation.t['word_freq_make'].copy()

def correlation_spam(colo, spam):
    count_corr = 0
    nb = 0
    for i in colo:
        if((spam[nb] == 1) and (i != 0.00)):
            count_corr += 1
        nb+=1
    return count_corr/len(spam)

def correlation_nonspam(colo, spam):
    count_corr = 0
    nb = 0
    for i in colo:
        if((spam[nb] == 0) and (i != 0.00)):
            count_corr += 1
        nb+=1
    return count_corr/len(spam)

for g in importation.t.columns:
    col = importation.t[g].copy()
    corrspam = correlation_spam(col, importation.valspam)
    corrnonspam = correlation_nonspam(col, importation.valspam)
    #if((abs(corrspam / corrnonspam) > 1.5) or (abs(corrnonspam / corrspam) < 0.25)):
        #print(g, corrspam, corrnonspam)
    if(corrspam < corrnonspam):
        print(g, corrspam, corrnonspam)

