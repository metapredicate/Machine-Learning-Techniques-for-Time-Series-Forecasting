import matplotlib
from matplotlib import pyplot
import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.svm import SVR
from datetime import datetime
import os
from pathlib import Path
import math

def mean_absolute_percentage_error(y_true, y_forecast):
    y_true, y_forecast = np.array(y_true), np.array(y_forecast)
    # if y_true == 0 :
    #     y_true = 0.001 # work around division by zero
    return np.mean(np.abs((y_true - y_forecast) / y_true)) * 100


# Load data (We will be using strict *nix path)
df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")
# df.head()

#Create the lists / X and y data set
features = ["T3", "T2"]
target = ["Appliances"]
# Define Train Test Split Ratio (as global variables for the time being)
train_split = 0.7
test_split = 0.3

# Convert date column in the appropriate format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
# df.head()

# Obtain the master dataset
master_df = df[["date"] + target + features].copy()

#add lags
newFeatures = []
num_lags = int(6)
for i in target + features:
    for k in range(1,num_lags+1):
        # Create lags
        master_df["{}_{}".format(str(i), str(k))] = master_df[i].shift(k)
        newFeatures.append("{}_{}".format(str(i), str(k)))




#Set tarin and test datasets
train_df  = master_df.head(math.floor(len(df) * train_split))
test_df = master_df.tail(math.floor(len(df) * test_split))

x_train_df = train_df.loc[:,features[0]]
y_train_df = train_df.loc[:,'Appliances']

x_test_df = test_df.loc[:,features[0]]
y_test_df = test_df.loc[:,'Appliances']
print(x_train_df)
x_train = []
y_train = []

x_test = []
y_test = []

for feature_i in x_train_df:
  newrow = []
  newrow.append(feature_i)
  x_train.append(newrow)
  
#Create the dependent data set 'y' as target
for target_i in y_train_df:
  newrow = target_i
  y_train.append(newrow)

for feature_i in x_test_df:
  newrow = []
  newrow.append(feature_i)
  x_test.append(newrow)
  
#Create the dependent data set 'y' as target
for target_i in y_test_df:
  newrow = target_i
  y_test.append(newrow)

print(x_train)

#create and train the svr model
reg = SVR(kernel='rbf', C=1e3, gamma=0.1).fit(x_train, y_train)
preds = reg.predict(x_train)



#Measure the model performance on the train set
resultant_train_MAE = mean_absolute_error(y_train, preds)
#text_file.write("resulant_train_MAE "+str(resultant_train_MAE)+ "\n")
resultant_train_MAPE = mean_absolute_percentage_error(y_train, preds)
#text_file.write("resultant_train_MAE "+str(resultant_train_MAPE)+ "\n")
print("Performance on Training Set (MAE) : {:.3f} ".format(resultant_train_MAE))
# Measure the model performance on the test set
preds_test = reg.predict(x_test)

resultant_test_MAE = mean_absolute_error(y_test, preds_test)
#text_file.write("resulant_test_MAE "+str(resultant_test_MAE)+ "\n")
resultant_test_MAPE = mean_absolute_percentage_error(y_test, preds_test)
#text_file.write("resulant_test_MAPE "+str(resultant_test_MAPE)+ "\n")
print("Performance on Test Set (MAE) : {:.3f} ".format(resultant_test_MAE))

# plot the actual data and the predicted data
pyplot.clf()
pyplot.plot(y_test)
pyplot.plot(preds_test, color='red')
#pathGraphTail = "/" + name + ".png"
#pathGraph = Path(pathHead+pathGraphTail)
#pyplot.savefig(pathGraph)
pyplot.show()