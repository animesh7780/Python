#TRAIN A CLASSIFIER TO KNOW THE FLOWER IS IRIS-VIRGINIA OR NOT

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris["data"][:, 3:]
y = (iris["target"] ==2).astype(np.int64)

#training the classifier
clf = LogisticRegression()
clf.fit(X, y)

example = clf.predict([[1.7]])
print(example)

#using matplotlib to plot the graph
X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_prob = clf.predict_proba(X_new)
plt.plot(X_new, y_prob[:, 1], "o-", label="Iris-Virginia")
plt.show()

# print(y)
# print(list(iris.keys()))
# print(iris['data'])
# print(iris['target'])
# print(iris['DESCR'])


