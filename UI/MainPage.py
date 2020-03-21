import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Log_Entry_Class import Log_Entry

#from Log_Book_Class import log_book
#from Log_Entry_Request_Class import Log_Entry_Request_Class

app = dash.Dash(__name__)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#colours that will be used throughout the UI
colors = {
    'main' : '#1a1c23',
    'log_book': '#22252b',
    'text': '#b2b2af',
    'graph':  '#21252c',
    'green': '#3d9970',
    'red': '#fc4136',
    'black': '#000000',
    'white' : '#FFFFFF'
}

styles = {
    'grey_text_on_black_background': {
        'color': colors['text'],
    }
}

dataset_choices = [
    'energydata_complete.csv',
    'monthly-sunspots.csv'
]

model_choices = [
    'Linear Regression'
]


#Html Layout
app.layout = html.Div(
    style = {'background-color': colors['white'],
            'color': colors['black'],},
    children = [

        #Heading 1
        html.H1(children='Machine Learning Techniques for Time Series Forecasting',
            style={
            'display': 'block',
            'color': colors['black'],
            'background-color': colors['white'],
            'padding': 5,
            'text-align': 'center',
            'font-size': 35
            },
        ),

        #Heading 2
        html.H2(children='Microsoft Project Group 6',
            style={
            'color': colors['black'],
            'background-color': colors['white'],
            'padding': 5,
            'text-align': 'center',
            'font-size': 15
            },
        ),

        html.Div([
            #Dataset dropdown label + dropdown
            html.Label(style = {'color': colors['black'], 'padding': 5}, children = ['Dataset']),
            dcc.Dropdown(
                id='Dataset-dropdown',
                style={
                    'color': colors['black']
                    },
                options=[
                    {'label': 'Energy Data', 'value': dataset_choices[0]},
                    {'label': 'Sunspots', 'value': dataset_choices[1]}
                ],
                placeholder='Select a Dataset',
                value='None',
            ),
        ],style={'width': '50%', 'display': 'inline-block', 'padding': '5'}),

        html.Div([
            #Model dropdown label + dropdown
            html.Label(style = {'color': colors['black'], 'padding': 5}, children = ['Model']),
            dcc.Dropdown(
                id='Model-dropdown',
                style={
                    'color': colors['black']
                    },
                options=[
                    {'label': 'Linear Regression', 'value': model_choices[0]},
                ],
                placeholder='Select a Dropdown',
                value='None',
            ),
        ],style={'width': '50%', 'display': 'inline-block', 'padding': '5'}),

        #Training Data Graph
        html.Div([
            # training data graph
            html.H3('Training data graph', style={'text-align': 'center'}),
            dcc.Loading(
                children = [
                    dcc.Graph(id='training-data-graph', style = {'background-color': colors['white']}),
                ],
                type = 'circle',
            ),
        ],style={'width': '50%', 'display': 'inline-block', 'padding': '5'}),

        #Forecasting Data Graph
        html.Div([
            # Forecasting data graph
            html.H3('Forecast data graph',style={'text-align': 'center'}),
            dcc.Loading(
                children = [
                    dcc.Graph(id='forecast-data-graph', style = {'background-color': colors['white']}),
                ],
                type = 'circle',
            ),
        ],style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}),
    ])


#Callback for both dropdowns
@app.callback([Output('training-data-graph', 'figure'),
            Output('forecast-data-graph', 'figure')],
            [Input('Dataset-dropdown', 'value'),
            Input('Model-dropdown', 'value')])
def update_graph(dataset_dropdown_value, model_dropdown_value):

    #If dropdown selected is a valid data
    if dataset_dropdown_value in dataset_choices and model_dropdown_value in model_choices:

        #Create a Log Entry
        log_entry = Log_Entry(model_dropdown_value, dataset_dropdown_value, '14/3/20', 1/2)

        #return log entry to training-data-graph
        return log_entry.training_graph, log_entry.forecasting_graph

    else:
        return go.Figure(), go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)
