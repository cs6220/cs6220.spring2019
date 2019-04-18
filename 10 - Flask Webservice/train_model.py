"""
To train this model, in your terminal:
> python train_model.py
"""

from sklearn import datasets
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeClassifier

print("Loading the Iris dataset...")
iris = datasets.load_iris()
X = iris.data
y = iris.target

print("Training a Decision Tree classifier...")
clf = DecisionTreeClassifier()
clf.fit(X, y)

print("Exporting the trained model...")
joblib.dump(clf, 'model/iris_classifier.joblib')

print("Done.")
