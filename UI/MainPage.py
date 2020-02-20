import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from datetime import datetime as dt
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

csv_path = 'monthly-sunspots.csv'

app.layout = html.Div([

    html.H1(
        children='Machine Learning Techniques for Time Series Forecasting '
    ),

    html.H2(
        children='Group 6'
    ),

    html.Label('Dataset dropdown'),
    dcc.Dropdown(
        id='Dataset-dropdown',
        options=[
            {'label': 'Dataset 1', 'value': csv_path },
            {'label': 'Dataset 2 ', 'value': csv_path},
            {'label': 'Dataset 3', 'value': csv_path}
        ],
        value='Dataset 1'
    ),

    html.Label('Model-dropdown'),
    dcc.Dropdown(
        id='Model-dropdown',
        options=[
            {'label': 'FFT', 'value': 'FFT'},
            {'label': 'Arima', 'value': 'ARIMA'},
            {'label': 'Deep learning', 'value': 'DEEPLEARNING'}
        ],
        value='FFT'
    ),

    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('Dataset-dropdown', 'value')])
def update_graph(selected_dropdown_value,):
    html.H1(children='selected_dropdown_value'),
    dataset = pd.read_csv(selected_dropdown_value, header=0, parse_dates=[0])
    df = px.dataset.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color='country')
    fig.show()

    fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)
