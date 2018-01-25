# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 08:11:44 2017

@author: kvan
"""
print("heloo")
import os
import numpy as np
import openpyxl
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
iris
iris.data #without header
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head(100)
df.to_excel("D:\Python\PyPractice\hihi.xlsx")
X,y=iris.data[:,:2], iris.target
iris.target

from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

lr = linear_model.LinearRegression()
boston = datasets.load_boston()
y = boston.target

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, boston.data, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()