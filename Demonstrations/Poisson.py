# Forecasting data via simulating a Poisson Process
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import numpy as np

csv_path = 'monthly-sunspots.csv'
dataset = pd.read_csv(csv_path, header=0, parse_dates=[0])

seriesLength = len(dataset.index)

SUM_LIST  = dataset["Sunspots"].tolist()
print("Total number of Entries: " + str(len(SUM_LIST)))
#print(SUM_LIST)
total = 0
for i in SUM_LIST:
    total += i
#print("total is: " + str(total))

# lambda - Event Rate
# k      - k is the value that our Discrete Random Variable takes on
# t      - time window (i.e. total number of entries in time series)
# d      - unit of time


def calculateLambda(k, t, d):
    return ( k / t ) * d
def poissonUnknownLambda(k, t, d):
    l = calculateLambda(k, t, d)
    return (np.exp(l) * (l**k) ) / math.factorial(k)
def poissonKnownLambda(k, l):
    return Decimal(math.exp(l)) * ( (Decimal(l)**Decimal(k)) / math.factorial(Decimal(k)))
def poissonProbability(timespan, lambda_):
    print("Our Timespan is: " + str(timespan))
    print("Our Lambda is: " + str(lambda_))
    x = 0
    temp = -timespan * lambda_
    print("temp est: "+str(temp))
    p = np.exp(temp)
    print(str(p))
    p *= (timespan*lambda_)**x
    print(str(p))
    ans = 1-p
    print(str(ans))

print( calculateLambda(total, seriesLength, 1))
###############################################################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.H1(
        children='Monthly Sunspots'
    ),
"""
    dcc.Graph(
        id='Month-vs-Sunspots',
        figure={
            'data': [

            ],
            'layout': dict(

            )
        }
    )
"""
])

if __name__ == '__main__':
    app.run_server(debug=True)