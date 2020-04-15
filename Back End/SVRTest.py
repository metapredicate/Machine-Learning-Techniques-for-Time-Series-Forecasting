# Load libraries
import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
import seaborn as sns
#matplotlib inline
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import r2_score, make_scorer
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")

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
features = ['lights', 'T1', 'RH_1', 'T2', 'RH_2', 'T3',
       'RH_3', 'T4', 'RH_4', 'T5', 'RH_5', 'T6', 'RH_6', 'T7', 'RH_7', 'T8',
       'RH_8', 'T9', 'RH_9', 'T_out', 'RH_out', 'Windspeed', 'Tdewpoint', 'hour']

# Define Train Test Split Ratio
train_split = 0.8
test_split = 0.2

# Obtain the master dataset
master_df = df[["date"] + target + features].copy()

lags = [5]
for j in lags:
    # Compute the lags of each and every variable
    newFeatures = []
    num_lags = int(j)
    if lagflag is True:
        for i in target:
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
            "C": [10]
            }
    
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

    #create and train the svr model
    reg = SVR(kernel='linear', C=0.1, gamma=0.1).fit(X_train, y_train.Appliances.ravel())
    preds = reg.predict(X_test)

    # Predict the performance in the test set
    #preds = optimal_model.predict(X_test)

    print("Performance on Test Set (MAE) : {:.3f} ".format(mean_absolute_error(preds, y_test.values.flatten())))
    print ("Number of lags used : " + str(j))