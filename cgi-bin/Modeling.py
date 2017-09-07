#! /usr/bin/env python

import cgi
from sklearn.externals import joblib
import numpy as np

data_arr0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # 50
# data_arr1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  # 0?????
# data_arr2 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # 16
# data_arr3 = np.array([0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  # 0 ??

form = cgi.FieldStorage()
# 0
firstVisit = form.getvalue("firstVisit")
data_arr0[0] = int(firstVisit)
# 1
haveAppointment = form.getvalue("haveAppointment")
data_arr0[1] = int(haveAppointment)
# 2
salesConsultant = form.getvalue("salesConsultant")
if salesConsultant:
    data_arr0[2] = 1
else:
    data_arr0[2] = 0
# 3
cityTier = form.getvalue("cityTier")
data_arr0[3] = int(cityTier)
# 4
arrivalTime = form.getvalue("arrivalTime")
data_arr0[4] = int(arrivalTime)
# 5
stayDuration = form.getvalue("stayDuration")
data_arr0[5] = int(stayDuration)
# 6
testDrive = form.getvalue("testDrive")
data_arr0[6] = int(testDrive)
# 7 - 14
category = form.getvalue("category")
data_arr0[int(category)+7] = 1
# 15 - 22
subRegion = form.getvalue("subRegion")
data_arr0[int(subRegion)+15] = 1
# 23
brand = form.getvalue("brand")
data_arr0[23] = int(brand)

data_arr = [data_arr0]


# load the prediction model
rf_joblib = joblib.load('./models/decision_tree.pkl')
#rf_joblib = joblib.load('./models/Magic_Mirror_Model.pkl')


# predict
y_pred_joblib = rf_joblib.predict(data_arr)
y_predprob_joblib = rf_joblib.predict_proba(data_arr)[:, 1]
y_predprob_joblib_indicator = rf_joblib.predict_proba(data_arr)[:, 0]
percentage = round(y_predprob_joblib[0] * 100, 2)
statement = "Very low possibility"
if percentage >= 90:
    statement = "Mostly likely"
elif percentage >= 70:
    statement = "Likely"
elif percentage >= 50:
    statement = "Perhaps"
elif percentage >= 35:
    statement = "Maybe"
elif percentage >= 20:
    statement = "Very low possibility"
else:
    statement = "Almost NO"

print("Content-type: text/html\n")

#print(str(y_pred_joblib) + " " + str(y_predprob_joblib_indicator) + " " + statement + " to buy: " + str(percentage) + "%")
#print(y_predprob_joblib_figure + "Figure" + statement + " to buy: " + str(percentage) + "%")

print(str(percentage) + "%" + "  probability to make a deal!")
