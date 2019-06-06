from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import train_test_split
from importation_pandas_noShuffle import importcsv



'''clAno = LocalOutlierFactor()
y_pred = clAno.fit_predict(X)
n_errors = (y_pred != y).sum




print(len(y_pred))'''



"""
============================================================================
Comparing anomaly detection algorithms for outlier detection on toy datasets
============================================================================

This example shows characteristics of different anomaly detection algorithms
on 2D datasets. Datasets contain one or two modes (regions of high density)
to illustrate the ability of algorithms to cope with multimodal data.

For each dataset, 15% of samples are generated as random uniform noise. This
proportion is the value given to the nu parameter of the OneClassSVM and the
contamination parameter of the other outlier detection algorithms.
Decision boundaries between inliers and outliers are displayed in black
except for Local Outlier Factor (LOF) as it has no predict method to be applied
on new data when it is used for outlier detection.

The :class:`sklearn.svm.OneClassSVM` is known to be sensitive to outliers and
thus does not perform very well for outlier detection. This estimator is best
suited for novelty detection when the training set is not contaminated by
outliers. That said, outlier detection in high-dimension, or without any
assumptions on the distribution of the inlying data is very challenging, and a
One-class SVM might give useful results in these situations depending on the
value of its hyperparameters.

:class:`sklearn.covariance.EllipticEnvelope` assumes the data is Gaussian and
learns an ellipse. It thus degrades when the data is not unimodal. Notice
however that this estimator is robust to outliers.

:class:`sklearn.ensemble.IsolationForest` and
:class:`sklearn.neighbors.LocalOutlierFactor` seem to perform reasonably well
for multi-modal data sets. The advantage of
:class:`sklearn.neighbors.LocalOutlierFactor` over the other estimators is
shown for the third data set, where the two modes have different densities.
This advantage is explained by the local aspect of LOF, meaning that it only
compares the score of abnormality of one sample with the scores of its
neighbors.

Finally, for the last data set, it is hard to say that one sample is more
abnormal than another sample as they are uniformly distributed in a
hypercube. Except for the :class:`sklearn.svm.OneClassSVM` which overfits a
little, all estimators present decent solutions for this situation. In such a
case, it would be wise to look more closely at the scores of abnormality of
the samples as a good estimator should assign similar scores to all the
samples.

While these examples give some intuition about the algorithms, this
intuition might not apply to very high dimensional data.

Finally, note that parameters of the models have been here handpicked but
that in practice they need to be adjusted. In the absence of labelled data,
the problem is completely unsupervised so model selection can be a challenge.
"""

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Albert Thomas <albert.thomas@telecom-paristech.fr>
# License: BSD 3 clause

import time

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn import svm
from sklearn.datasets import make_moons, make_blobs
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

print(__doc__)




def find_anomalies(nameAlgorithm):

    matplotlib.rcParams['contour.negative_linestyle'] = 'solid'

    # Example settings
    n_samples = 300
    outliers_fraction = 0.15
    n_outliers = int(outliers_fraction * n_samples)
    n_inliers = n_samples - n_outliers


    setX, setY = importcsv()
    X= setX.values.tolist()
    y = setY
    #X, X_t, y, y_t = train_test_split(setX, setY, test_size=0.05)


    # define outlier/anomaly detection methods to be compared
    anomaly_algorithms = [
        ("Robust covariance", EllipticEnvelope(contamination=outliers_fraction)),
        ("One-Class SVM", svm.OneClassSVM(nu=outliers_fraction, kernel="rbf",
                                          gamma=0.1)),
        ("Isolation Forest", IsolationForest(behaviour='new',
                                             contamination=outliers_fraction,
                                             random_state=42)),
        ("Local Outlier Factor", LocalOutlierFactor(
            n_neighbors=35, contamination=outliers_fraction))]


    X_Spam = []
    X_spam_nb = []


    for k in range(len(X)):

        if y[k] == 0:
            X_Spam.append(X[k])
            X_spam_nb.append(k)

    #print(len(X_Spam))




    # Add outliers


    for name, algorithm in anomaly_algorithms:

        #print(name)
        if name == nameAlgorithm:
            t0 = time.time()
            algorithm.fit(X_Spam)
            t1 = time.time()
            #plt.subplot(len(datasets), len(anomaly_algorithms), plot_num)
            '''if i_dataset == 0:
                plt.title(name, size=18)
            '''

            # fit the data and tag outliers
            if name == "Local Outlier Factor":
                y_pred = algorithm.fit_predict(X_Spam)
            else:
                y_pred = algorithm.fit(X).predict(X_Spam)



            nbAno = 0
            resultAnoSpam = []
            for k in range(len(y_pred)):
                if y_pred[k] == -1:
                    nbAno+=1

                    resultAnoSpam.append(X_spam_nb[k])
            #print(resultAnoSpam)
            #print(nbAno)












    # Example settings

    outliers_fraction = 0.15

    setX, setY = importcsv()
    X= setX.values.tolist()
    y = setY
    #X, X_t, y, y_t = train_test_split(setX, setY, test_size=0.05)


    # define outlier/anomaly detection methods to be compared
    anomaly_algorithms = [
        ("Robust covariance", EllipticEnvelope(contamination=outliers_fraction)),
        ("One-Class SVM", svm.OneClassSVM(nu=outliers_fraction, kernel="rbf",
                                          gamma=0.1)),
        ("Isolation Forest", IsolationForest(behaviour='new',
                                             contamination=outliers_fraction,
                                             random_state=42)),
        ("Local Outlier Factor", LocalOutlierFactor(
            n_neighbors=35, contamination=outliers_fraction))]

    X_Non_Spam = []
    X_Non_Spam_nb = []

    for k in range(len(X)):

        if y[k] == 1:
            X_Non_Spam.append(X[k])
            X_Non_Spam_nb.append(k)

    #print(len(X_Non_Spam))




    # Add outliers


    for name, algorithm in anomaly_algorithms:
        #print(name)
        if name == nameAlgorithm:
            t0 = time.time()
            algorithm.fit(X_Non_Spam)
            t1 = time.time()
            #plt.subplot(len(datasets), len(anomaly_algorithms), plot_num)
            '''if i_dataset == 0:
                plt.title(name, size=18)
            '''

            # fit the data and tag outliers
            if name == "Local Outlier Factor":
                y_pred = algorithm.fit_predict(X_Non_Spam)
            else:
                y_pred = algorithm.fit(X).predict(X_Non_Spam)

            nbAno = 0

            if name == nameAlgorithm:
                resultAno_NotSpam = []
                for k in range(len(y_pred)):
                    if y_pred[k] == -1:
                        nbAno+=1
                        resultAno_NotSpam.append(X_Non_Spam_nb[k])
                #print(resultAno_NotSpam)
                #print(nbAno)




    return resultAnoSpam + resultAno_NotSpam



#find_anomalies("Isolation Forest")








