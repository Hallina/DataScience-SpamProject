import importation

from sklearn.svm import LinearSVC
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import RobustScaler

from sklearn.feature_selection import SelectFromModel

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split

train, test = train_test_split(importation.t, test_size=0.5)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.5)


clf = SelectKBest(chi2, k=6)

print("start train...")

x = clf.fit_transform(train, spamtrain)
