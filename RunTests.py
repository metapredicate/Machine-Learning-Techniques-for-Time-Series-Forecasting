import pandas as pd
from Regression import run_test

# load data 
df = pd.read_csv("./Data/Appliances Energy Usage Prediction/energydata_complete.csv")

# Convert date column in the appropriate format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

target = ["Appliances"]
# headers = list(df.columns.values)
# headers = headers[2:] # remove the date and target variable column
# features = []
# features = [ headers[1] ]
features = [ 
    "rv1", "RH_1", "Press_mm_hg", "RH_3", "RH_5",
    "T3", "RH_8", "T8", "T6", "RH_2",
    "T8", "T6", "RH_2", "RH_out", "RH_9",
    "Windspeed", "RH_7", "T2", "T4", "RH_4",
    "Visibility", "RH_6", "T5", "Tdewpoint", "T1",
    "T7", "T_out", "lights", "T9" ]

for i in range(0,len(features)-1):
    tempFeatures = features[0:i]
    # if ( i != 1):
    #     features = features.append(i)
    run_test(df, target, tempFeatures, 0.7, 5)

# features = ["lights", "T1", "T2", "T3"]

# TESTING Number of Lags
# for i in range(0,1):
#     run_test(df, target, features, 0.7, i)