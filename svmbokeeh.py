import importation

from sklearn import svm
from sklearn import metrics
from sklearn import preprocessing

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.pipeline import make_pipeline

from bokeh.plotting import figure as bokehFigure
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.io import show as bokehShow

train, test = train_test_split(importation.t, test_size=0.1)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.1)

clf = make_pipeline(preprocessing.StandardScaler(), svm.SVC(C=1, gamma=80000))

clf.fit(train, spamtrain)

expected = spamtest
predicted = clf.predict(test)

print(clf.score(train, spamtrain))

# add data to bokeh
sourcetrain = ColumnDataSource(train)
sourcetest = ColumnDataSource(test)

# création vue
p = bokehFigure()
p.circle(x="capital_run_length_total", y="char_freq_!", source=sourcetrain, color = 'navy')
p.circle(x="capital_run_length_total", y="char_freq_!", source=sourcetest, color= 'red')

bokehShow(p)
