import importation

from sklearn.linear_model import BayesianRidge, LinearRegression

from sklearn import svm
from sklearn import metrics

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.io import show as bokehShow

train, test = train_test_split(importation.t, test_size=0.2)
spamtrain, spamtest = train_test_split(importation.valspam, test_size=0.2)


clf = BayesianRidge(compute_score=True)
ols = LinearRegression()

clf.fit(train, spamtrain)
ols.fit(train, spamtrain)



expected = spamtest

predicted = clf.predict(test)
predicted1 = ols.predict(test)


#print(spamtrain)

#print(predicted)


print(clf.score(test, spamtest))
print(ols.score(test, spamtest))


# Create a blank figure with labels
p = figure(plot_width = 600, plot_height = 600, 
           title = 'Example Glyphs',
           x_axis_label = 'X', y_axis_label = 'Y')



# Add squares glyph
p.square(clf.X_offset_, ols.coef_, size = 12, color = 'navy', alpha = 0.6)

bokehShow(p)
