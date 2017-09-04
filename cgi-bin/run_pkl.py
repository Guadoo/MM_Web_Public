# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:29:31 2017

@author: GUANGWU
"""
from sklearn.externals import joblib
import numpy as np
import pandas as pd

#data = pd.read_csv('X_test_df.csv')
#data = data.drop([data.columns[0]], axis=1)
#data_arr = np.array(data)

# replace by actual sample
data_arr = np.array([0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1])

# load the prediction model
rf_joblib = joblib.load('../models/decision_tree.pkl')

# predict 
y_pred_joblib = rf_joblib.predict(data_arr) 
y_predprob_joblib = rf_joblib.predict_proba(data_arr)[:,1]

print(y_predprob_joblib[0])


