# from collections import namedtuple
import matplotlib
from matplotlib import pyplot
import pandas as pd
import numpy as np
import datetime
# from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from datetime import datetime
import os
from pathlib import Path
import errno
from sklearn.model_selection import KFold

def mean_absolute_percentage_error(y_true, y_forecast):
    y_true, y_forecast = np.array(y_true), np.array(y_forecast)
    # if y_true == 0 :
    #     y_true = 0.001 # work around division by zero
    return np.mean(np.abs((y_true - y_forecast) / y_true)) * 100

# load data 
df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")

# Convert date column in the appropriate format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')


def run_test(dataframe, target, features, train_split, num_lags, folds):

    folds = KFold(n_splits=folds)

    # Obtain the master dataset
    master_df = df[["date"] + target + features].copy()

    for train_index, test_index in folds.split(master_df, master_df[target]):
        X_train = master_df.iloc[train_index].copy()
        X_test = master_df.iloc[test_index].copy()
        Y_train = master_df.iloc[train_index].copy()
        Y_test = master_df.iloc[test_index].copy()

        # Compute the lags of each and every variable
        newFeatures = []
        num_lags = int(num_lags)
        if num_lags != 0:
            for i in target + features:
                for k in range(1,num_lags+1):
                    # Create lags
                    X_train["{}_{}".format(str(i), str(k))] = X_train[i].shift(k)
                    Y_train["{}_{}".format(str(i), str(k))] = X_test[i].shift(k)
                    newFeatures.append("{}_{}".format(str(i), str(k)))

                     # Drop Missing Values
                    X_train = master_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
                    Y_train = master_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        
        X_train = X_train[:][features].copy()
        Y_train = Y_train[:][target].copy()
        X_test = X_test[:][features].copy()
        Y_test = Y_test[:][target].copy()
        

        # Perform Linear Regression on the training data and Predict
        reg = LinearRegression().fit(X_train, Y_train)
        preds = reg.predict(X_train)

        # Measure the model performance on the test set
        preds_test = reg.predict(X_test)
        resultant_test_MAE = mean_absolute_error(Y_test, preds_test)
        print("Performance on Test Set (MAE) : {:.3f} ".format(resultant_test_MAE))
    

        


if __name__ == "__main__":
    # Define the features and target variables
    target = ["Appliances"]
    features = ["lights", "T1", "T2", "T3"]
    run_test(df, target, features, 0.7, 6, 5)
    pass
