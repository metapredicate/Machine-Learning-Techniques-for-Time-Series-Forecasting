import pandas as pd
from Regression import run_test

# load data 
df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")

# Convert date column in the appropriate format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

target = ["Appliances"]
headers = list(df.columns.values)
headers = headers[2:] # remove the date and target variable column
features = []
# features = [ headers[1] ]

for i in headers:
    features = [i]
    # if ( i != 1):
    #     features = features.append(i)
    run_test(df, target, features, 0.7, 11)

# features = ["lights", "T1", "T2", "T3"]

# TESTING Number of Lags
# for i in range(0,1):
#     run_test(df, target, features, 0.7, i)