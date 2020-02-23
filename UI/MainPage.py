import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime as dt
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
df = pd.read_csv("monthly-sunspots.csv")

#Html Layout
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
            {'label': 'Sunspots', 'value': "monthly-sunspots.csv"},
            {'label': 'Sunspots', 'value': "monthly-sunspots.csv"},
            {'label': 'Sunspots', 'value': "monthly-sunspots.csv"}
        ],
        value="monthly-sunspots.csv"
    ),

    html.Label('Model-dropdown'),
    dcc.Dropdown(
        id='Model-dropdown',
        options=[
            {'label': 'FFT', 'value': 'FFT'},
            {'label': 'Arima', 'value': 'ARIMA'},
            {'label': 'Deep learning', 'value': 'DEEPLEARNING'}
        ],
        value=''
    ),
    dcc.Graph(id='my-graph')

], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('Dataset-dropdown', 'value')])
def update_graph(selected_dropdown_value,):
    #Graph Code
    fig = go.Figure()
    df = pd.read_csv("monthly-sunspots.csv")
    fig.add_trace(go.Scatter(x=df.Month, y=df['Sunspots'], name="Sunspots",
                            line_color='deepskyblue'))
    fig.update_layout(title_text='Sunspots Time Series with Rangeslider',
                    xaxis_rangeslider_visible=True)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
