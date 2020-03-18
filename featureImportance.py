# plot feature importance manually
import numpy as np
from np import loadtxt
from xgboost import XGBClassifier
from matplotlib import pyplot
import pandas as pd
from sklearn.model_selection import train_test_split
# load data

trainingData =r'C:\\Users\\hurri\Desktop\\SWENG\Data\\Electric Devices\\ElectricDevices_TRAIN.csv'
dataset = pd.read_csv(trainingData, engine='python')
dataset = dataset.drop(["date"], axis = 1)
X = dataset.iloc[:,0:8]
y = dataset.iloc[:,8]
model = XGBClassifier()
model.fit(X, y)
# feature importance
print(model.feature_importances_)
# plot
pyplot.bar(range(len(model.feature_importances_)), model.feature_importances_)
pyplot.show()