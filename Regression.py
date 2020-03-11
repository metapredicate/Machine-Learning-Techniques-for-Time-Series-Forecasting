# Load libraries
import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def mean_absolute_percentage_error(y_true, y_forecast):
    y_true, y_forecast = np.array(y_true), np.array(y_forecast)
    # if y_true == 0 :
    #     y_true = 0.001 # work around division by zero
    return np.mean(np.abs((y_true - y_forecast) / y_true)) * 100




# Load data (We will be using strict *nix path)
df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")
# df.head()

# Convert date column in the appropriate format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
# df.head()

# Define the features and target variables
target = ["Appliances"]
features = ["lights", "T1", "T2", "T3"]

# Define Train Test Split Ratio (as global variables for the time being)
train_split = 0.7
test_split = 0.3

# Obtain the master dataset
master_df = df[["date"] + target + features].copy()
# master_df.head()

# Compute the lags of each and every variable
newFeatures = []
num_lags = int(6)
for i in target + features:
    for k in range(1,num_lags+1):
        # Create lags
        master_df["{}_{}".format(str(i), str(k))] = master_df[i].shift(k)
        newFeatures.append("{}_{}".format(str(i), str(k)))
# master_df.head()

df[target].plot()

master_df[["date","Appliances","Appliances_1","Appliances_2"]].head()

# Drop Missing Values
master_df = master_df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# master_df.head()

# Split dataset into train/ test set
train_records = int(np.round(train_split * master_df.shape[0]))
test_records = int(master_df.shape[0]-train_records)

X_train = master_df[:train_records][newFeatures].copy()
y_train = master_df[:train_records][target].copy()

X_test = master_df[-test_records:][newFeatures].copy()
y_test = master_df[-test_records:][target].copy()

X_train.shape
y_test.shape

reg = LinearRegression().fit(X_train, y_train)
preds = reg.predict(X_train)

# Measure the model performance on the train set
print("Performance on Training Set (MAE) :",mean_absolute_error(y_train, preds))
print("Performance on Training Set (MAPE):{} %".format(mean_absolute_percentage_error(y_train, preds)))
# Measure the model performance on the test set
preds_test = reg.predict(X_test)
print("Performance on Test Set (MAE) :",mean_absolute_error(y_test, preds_test))
print("Performance on Test Set (MAPE): {} %".format(mean_absolute_percentage_error(y_test, preds_test)))