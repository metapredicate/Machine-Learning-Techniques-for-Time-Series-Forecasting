# Load libraries
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import os
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib
from matplotlib import pyplot
from pathlib import Path
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
import seaborn as sns
#matplotlib inline
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import r2_score, make_scorer
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("../Data/Appliances Energy Usage Prediction/energydata_complete.csv")

# create log file for results 
# if(moniker == ""):
#     name = "Test "+str(datetime.now())
# else:
#     name = "/Test "+str(datetime.now()) + "/" + moniker + "/"
name = "Test "+str(datetime.now())
pathHead = "./test_results/" + name
print(pathHead)
try:
    os.makedirs(pathHead)
    print("Directory ", pathHead, " Created ")
except OSError as e:
    if(e.errno == errno.EEXIST):
        print("Directory ", pathHead, " already exists.")
    else:
        raisenow = datetime.now()
pathOutputTail = "/Output-" + name + ".txt"
pathOutput = Path(pathHead + pathOutputTail)
text_file = open(str(pathOutput), "w")


# Compute Lags
lagflag = True

df.head()

# Convert date column in the appropriate format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
# Extract the day of the week as a feature
df['day'] = pd.to_datetime(df['date']).dt.dayofweek

# Extract hour of the day
df['hour'] = pd.to_datetime(df['date']).dt.hour

# Define the features and target variables
target = ["Appliances"]
features = ['lights', 'T1','T2','RH_6', 'Press_mm_hg', 'T_out', 'RH_out', 'Windspeed', 'Tdewpoint', 'hour']

# Define Train Test Split Ratio
train_split = 0.8
test_split = 0.2

# Obtain the master dataset
master_df = df[["date"] + target + features].copy()

# Compute the lags of each and every variable
newFeatures = []
num_lags = int(4)
if lagflag is True:
    for i in target + features:
        for k in range(1,num_lags+1):
            # Create lags
            master_df["{}_{}".format(str(i), str(k))] = master_df[i].shift(k)
            newFeatures.append("{}_{}".format(str(i), str(k)))
else:
    newFeatures = features

features = newFeatures + features

# Drop Missing Values
master_df = master_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# Split dataset into train/ test set
train_records = int(np.round(train_split * master_df.shape[0]))
test_records = int(master_df.shape[0]-train_records)

X_train = master_df[:train_records][features].copy()
y_train = master_df[:train_records][target].copy()

X_test = master_df[-test_records:][features].copy()
y_test = master_df[-test_records:][target].copy()

params = {"gamma": [0.1],
        "kernel": ["linear"],
        "C": [0.1]}

# Make cv scorer
#score = make_scorer(r2_score, greater_is_better=True)

# Create an object to perform time series cross validation
#tscv  = TimeSeriesSplit(n_splits=2)
# Define Model
#model = SVR()
# Perform Grid Search
#gsearch = GridSearchCV(estimator=model, cv=tscv, param_grid=params, scoring = score, n_jobs = 1, verbose = 2)

#optimal_model = gsearch.fit(X_train, y_train.Appliances.ravel())
#print(optimal_model.best_estimator_)

text_file.write("Number of Lags = "+str(num_lags)+"\n")
text_file.write("Number of Features we are using: "+str(len(features)) + "\n")
text_file.write("Features we are using = "+str(features)+"\n")

#create and train the svr model
reg = SVR(kernel='linear', C=0.1, gamma=0.1).fit(X_train, y_train.Appliances.ravel())
preds = reg.predict(X_test)

#plot the actual data and the predicted data
pyplot.clf()
X1 = np.linspace(0, y_test.size, y_test.size)
pyplot.plot(X1, y_test)
X2 = np.linspace(0, preds.size, preds.size)
pyplot.plot(X2,preds, color='red')
pathGraphTail = "/" + name + ".png"
pathGraph = Path(pathHead+pathGraphTail)
pyplot.savefig(pathGraph)
pyplot.show()

# Predict the performance in the test set
#preds = optimal_model.predict(X_test)
print("Performance on Test Set (MAE) : {:.3f} ".format(mean_absolute_error(preds, y_test.values.flatten())))
print ("Number of lags used : " + str(4))
