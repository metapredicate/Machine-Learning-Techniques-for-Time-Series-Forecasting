# imports...
import matplotlib
from matplotlib import pyplot
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from datetime import datetime
import os
from pathlib import Path

def linear_regression(dataframe, train_split):
    
    # Set the target variable
    target = ["Appliances"]

    # Set features
    features = ["lights", "T1", "T2", "T3"]

    # Convert date column in the appropriate format
    dataframe['date'] = pd.to_datetime(dataframe['date'], format='%Y-%m-%d %H:%M:%S')

    # Obtain the master dataset
    master_df = dataframe[["date"] + target + features].copy()

    # Compute the lags of each and every variable
    newFeatures = []
    num_lags = 6
    num_lags = int(num_lags)
    if num_lags != 0:
        for i in target + features:
            for k in range(1,num_lags+1):
                # Create lags
                master_df["{}_{}".format(str(i), str(k))] = master_df[i].shift(k)
                newFeatures.append("{}_{}".format(str(i), str(k)))

    # Drop Missing Values
    master_df = master_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

    # Partition the dataset into Train and Test sets
    train_records = int(np.round(train_split * master_df.shape[0]))
    test_records = int(master_df.shape[0]-train_records)
    X_train = master_df[:train_records][newFeatures].copy()
    y_train = master_df[:train_records][target].copy()
    X_test = master_df[-test_records:][newFeatures].copy()
    y_test = master_df[-test_records:][target].copy()

    # Perform Linear Regression on the training data and Predict
    reg = LinearRegression().fit(X_train, y_train)
    preds = reg.predict(X_train)   

    # Measure the model performance on the train set
    resultant_train_MAE = mean_absolute_error(y_train, preds)
    print("Performance on Training Set (MAE) : {:.3f} ".format(resultant_train_MAE))

    # Measure the model performance on the test set
    preds_test = reg.predict(X_test)
    resultant_test_MAE = mean_absolute_error(y_test, preds_test)
    print("Performance on Test Set (MAE) : {:.3f} ".format(resultant_test_MAE))

    # Append the prediction data as another column at the end of the dataframe
    results = pd.DataFrame(preds_test)
    dataframe["Results"] = results
    return dataframe

if __name__ == "__main__":
    # load data 
    df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")
    # Define the features and target variables
    target = ["Appliances"]
    
    linear_regression(df, 0.7)
    pass