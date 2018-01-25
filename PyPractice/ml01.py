import numpy as np

import matplotlib as plt

from sklearn import datasets

from sklearn import metrics

from sklearn.linear_model import LogisticRegression

dataset = datasets.load_iris()

model.fit(dataset.data, dataset.target)

expected = dataset.target

predicted = model.predict(dataset.data)

print(metrics.classification_report(expected, predicted))

print(metrics.confusion_matrix(expected, predicted))