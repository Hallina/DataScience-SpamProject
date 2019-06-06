from importation_pandas import importcsv

import matplotlib
import seaborn
import pandas
import matplotlib.dates as md
from matplotlib import pyplot as plt

from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM

data, spam = importcsv()

data = data[1814:]

spam = spam[1814:]

# some function for later

# return Series of distance between each point and his distance with the closest centroid
def getDistanceByPoint(data, model):
    distance = pd.Series()
    for i in range(0,len(data)):
        Xa = np.array(data.loc[i])
        Xb = model.cluster_centers_[model.labels_[i]-1]
        distance.set_value(i, np.linalg.norm(Xa-Xb))
    return distance

# train markov model to get transition matrix
def getTransitionMatrix (df):
	df = np.array(df)
	model = msm.estimate_markov_model(df, 1)
	return model.transition_matrix

def markovAnomaly(df, windows_size, threshold):
    transition_matrix = getTransitionMatrix(df)
    real_threshold = threshold**windows_size
    df_anomaly = []
    for j in range(0, len(df)):
        if (j < windows_size):
            df_anomaly.append(0)
        else:
            sequence = df[j-windows_size:j]
            sequence = sequence.reset_index(drop=True)
            df_anomaly.append(anomalyElement(sequence, real_threshold, transition_matrix))
    return df_anomaly



# Take useful feature and standardize them
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data)
data1 = pandas.DataFrame(np_scaled)
# reduce to 2 importants features

#on remet les colonnes

#data_info = pandas.DataFrame(data=data1, columns=data.columns)
nbComponent = 5

pca_info = PCA(n_components=nbComponent)
pca_info.fit_transform(data, spam)

for i in range(0, nbComponent):
    print("feature " + str(i) + " ( "
      + data.columns[pca_info.components_[i].argmax()] + " ) : "
      + str(pca_info.components_[i][pca_info.components_[i].argmax()]))



pca = PCA(n_components=2)
data1 = pca.fit_transform(data1, spam)
# standardize these 2 new features
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data1)
data2 = pandas.DataFrame(np_scaled)
data1 = pandas.DataFrame(data1)

# visu 1
n_cluster = range(1, 20)
kmeans = [KMeans(n_clusters=i).fit(data1) for i in n_cluster]
kmeans1 = [KMeans(n_clusters=i).fit(data2) for i in n_cluster]
#scores = [kmeans[i].score(data1) for i in range(len(kmeans))]
#fig, ax = plt.subplots()
#ax.plot(n_cluster, scores)
#plt.show()

#prep visu 2
df = pandas.DataFrame()
cl1 = kmeans[4].predict(data1)
df['cluster'] = cl1
df['principal_feature1'] = data1[0]
df['principal_feature2'] = data1[1]
df['cluster'].value_counts()

#prep visu 2
df1 = pandas.DataFrame()
cl2 = kmeans1[4].predict(data2)
df1['cluster'] = cl2
df1['principal_feature1'] = data1[0]
df1['principal_feature2'] = data1[1]
df1['cluster'].value_counts()

#visu 2
#plot the different clusters with the 2 main features
fig, ax = plt.subplots()
colors = {0:'red', 1:'blue', 2:'green', 3:'pink', 4:'black'}
ax.scatter(df['principal_feature1'], df['principal_feature2'], c=df["cluster"].apply(lambda x: colors[x]))

fig1, ax1 = plt.subplots()
colors1 = {0:'red', 1:'blue', 2:'green', 3:'pink', 4:'black'}
ax1.scatter(df1['principal_feature1'], df1['principal_feature2'], c=df1["cluster"].apply(lambda x: colors1[x]))

plt.show()
