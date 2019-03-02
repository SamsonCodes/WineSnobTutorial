# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 07:36:17 2018

@author: Samson
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:01:36 2018

@author: Samson
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib


#3 Load red wine data
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')
print('loaded data!')


#4 Split data into training and test sets
y = data.quality
X = data.drop('quality', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123,stratify=y)
scaler = preprocessing.StandardScaler().fit(X_train)


#5 Declare data preprocessing steps
pipeline = make_pipeline(preprocessing.StandardScaler(), RandomForestRegressor(n_estimators=100))


#X Load model
clf = joblib.load('rf_regressor.pkl')
print('loaded model!')


#9 Evaluate model pipeline on test data
y_pred = clf.predict(X_test)
print("r2=" + str(r2_score(y_test, y_pred)))
print("mse=" + str(mean_squared_error(y_test, y_pred)))
y_pred = list(y_pred)
y_test = list(y_test)

correct = 0
for x in range(0, len(y_test)):
    if round(y_pred[x]) == round(y_test[x]):
        correct += 1
    else:        
        print("False prediction: " + str(round(y_test[x])) + " --> " + str(round(y_pred[x])))
print("Accuracy = " + str(correct/len(y_test)))
print('done!')