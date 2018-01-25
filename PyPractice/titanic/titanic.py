
# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd
import xgboost as xgb

# visualization
import matplotlib.pyplot as plt
#%matplotlib inline

# machine learning
import sklearn

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold


train_df = pd.read_csv('D:\Python\PyPractice\\titanic\\train.csv')
test_df = pd.read_csv('D:\Python\PyPractice\\titanic\\test.csv')
combine = [train_df, test_df]

print(train_df.columns.values)
print(test_df.columns.values)

