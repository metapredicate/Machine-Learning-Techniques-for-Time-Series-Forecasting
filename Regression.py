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

def mean_absolute_percentage_error(y_true, y_forecast):
    y_true, y_forecast = np.array(y_true), np.array(y_forecast)
    # if y_true == 0 :
    #     y_true = 0.001 # work around division by zero
    return np.mean(np.abs((y_true - y_forecast) / y_true)) * 100

# load data 
df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")

# Convert date column in the appropriate format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')


def run_test(dataframe, target, features, train_split, num_lags):
    # break conditions

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
    
    # Define Train Test Split Ratio
    test_split = 1 - train_split

    # Obtain the master dataset
    master_df = df[["date"] + target + features].copy()

    # Compute the lags of each and every variable
    newFeatures = []
    num_lags = int(num_lags)
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

    # Infomation written to the log files (for test purposes)
    text_file.write("Number of Lags = "+str(num_lags)+"\n")
    text_file.write("Features we are using = "+str(features)+"\n")

    # Measure the model performance on the train set
    resultant_train_MAE = mean_absolute_error(y_train, preds)
    text_file.write("resulant_train_MAE "+str(resultant_train_MAE)+ "\n")
    resultant_train_MAPE = mean_absolute_percentage_error(y_train, preds)
    text_file.write("resultant_train_MAPE "+str(resultant_train_MAPE)+ "\n")
    print("Performance on Training Set (MAE) : {:.3f} ".format(resultant_train_MAE))
    print("Performance on Training Set (MAPE): {:.3f} %".format(resultant_train_MAPE ))
    # Measure the model performance on the test set
    preds_test = reg.predict(X_test)

    resultant_test_MAE = mean_absolute_error(y_test, preds_test)
    text_file.write("resulant_test_MAE "+str(resultant_test_MAE)+ "\n")
    resultant_test_MAPE = mean_absolute_percentage_error(y_test, preds_test)
    text_file.write("resulant_test_MAPE "+str(resultant_test_MAPE)+ "\n")
    print("Performance on Test Set (MAE) : {:.3f} ".format(resultant_test_MAE))
    print("Performance on Test Set (MAPE): {:.3f}  %".format(resultant_test_MAPE))

    # Plotting is not so useful to us right now until we think of a fix.
    # plot the actual data and the predicted data
    # pyplot.clf()
    # pyplot.plot(y_test)
    # pyplot.plot(preds_test, color='red')
    # pathGraphTail = "/" + name + ".png"
    # pathGraph = Path(pathHead+pathGraphTail)
    # pyplot.savefig(pathGraph)
    # pyplot.show()

# try:
#     pyplot.clf()
#     pyplot.plot(preds.values)
#     pyplot.plot(preds_test, color='red')
#     pathGraphTail = "/" + name + ".png"
#     pathGraph = Path(pathHead+pathGraphTail)
#     pyplot.savefig(pathGraph)
#     pyplot.show()
# except:
#     pass
# with open('errors.txt', "a") as errors:
#     s = "" + name + " " + str(resultant_test_MAPE) + "\n"
#     errors.write(s)

if __name__ == "__main__":
    # Define the features and target variables
    target = ["Appliances"]
    features = ["lights", "T1", "T2", "T3"]
    run_test(df, target, features, 0.7, 6)
    pass