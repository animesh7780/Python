from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# load dataset
iris = datasets.load_iris()


features = iris.data
labels = iris.target

# print(features[0], labels[0])

#training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

#testing the classifier
a = float(input("Sepal Length: "))
b = float(input("Sepal Width: "))
c = float(input("Petal Length: "))
d = float(input("Petal Width: "))
preds = clf.predict([[a, b, c, d]])
print(preds)