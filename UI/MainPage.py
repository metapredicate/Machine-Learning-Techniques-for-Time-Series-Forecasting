import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime as dt
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# turn file into data frame
df = pd.read_csv("energydata_complete.csv")

#Html Layout
app.layout = html.Div([

    #Heading 1
    html.H1(
        children='Machine Learning Techniques for Time Series Forecasting '
    ),
    #Heading 2
    html.H2(
        children='Energy Data Time Series'
    ),

    #Dataset dropdown label + dropdown
    html.Label('Dataset'),
    dcc.Dropdown(
        id='Dataset-dropdown',
        options=[
            {'label': 'Appliances', 'value': 'Appliances'},
            {'label': 'lights', 'value': 'lights'},
            {'label': 'T1', 'value': 'T1'},
            {'label': 'RH_1', 'value': 'RH_1'},
            {'label': 'T2', 'value': 'T2'},
            {'label': 'RH_2', 'value': 'RH_2'},
            {'label': 'RH_3', 'value': 'T3'},
            {'label': 'RH_3', 'value': 'RH_3'},
            {'label': 'T4', 'value': 'T4'},
            {'label': 'RH_4', 'value': 'RH_4'},
            {'label': 'T5', 'value': 'T5'},
            {'label': 'RH_5', 'value': 'RH_5'},
            {'label': 'T6', 'value': 'T6'},
            {'label': 'RH_6', 'value': 'RH_6'},
            {'label': 'T7', 'value': 'T7'},
            {'label': 'RH_7', 'value': 'RH_7'},
            {'label': 'T8', 'value': 'T8'},
            {'label': 'RH_8', 'value': 'RH_8'},
            {'label': 'T9', 'value': 'T9'},
            {'label': 'RH_9', 'value': 'RH_9'},
            {'label': 'T_out', 'value': 'T_out'},
            {'label': 'Press_mm_hg', 'value': 'Press_mm_hg'},
            {'label': 'RH_out', 'value': 'RH_out'},
            {'label': 'Windspeed', 'value': 'Windspeed'},
            {'label': 'Visibility', 'value': 'Visibility'},
            {'label': 'Tdewpoint', 'value': 'Tdewpoint'},
            {'label': 'rv1', 'value': 'rv1'},
            {'label': 'rv2', 'value': 'rv2'}
        ],
        value = 'Appliances',
        placeholder="Select a Dataset",
    ),

    #Model Dropdown label + dropdown
    html.Label('Model'),
    dcc.Dropdown(
        id='Model-dropdown',
        options=[
            {'label': 'FFT', 'value': 'FFT'},
            {'label': 'Arima', 'value': 'ARIMA'},
            {'label': 'Deep learning', 'value': 'DEEPLEARNING'}
        ],
        placeholder="Select a Model",
    ),

    # input data graph
    dcc.Graph(id='input-data-graph'),

])

#Callback for Dataset dropdown
@app.callback(Output('input-data-graph', 'figure'), [Input('Dataset-dropdown', 'value')])
def update_graph(selected_dropdown_value,):
    #Graph Code
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.date, y=df[selected_dropdown_value], name = selected_dropdown_value, line_color='deepskyblue'))
    fig.update_layout(title_text='Input Data with Rangeslider', xaxis_rangeslider_visible=True,)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
