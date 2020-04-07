import time
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from Log_Book_Class import Log_Book
from Log_Entry_Class import Log_Entry
from Log_Entry_Request_Class import Log_Entry_Request
from dash.dependencies import Output, Input

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#app.config['suppress_callback_exceptions'] = True

model_dict = {'Energy Data': ['Linear Regression', 'Support Vector Regression','Random Forest Regression'], 'Sunspots': ['SARIMAX', 'SARIMA']}
models = list(model_dict.keys())

log_entry_dict = {}
log_entries = []

################################################################################
############################### GLOBALS ########################################
################################################################################

# Colours that will be used throughout the UI
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
        'background-color': colors['main']
    }
}

dataset_choices = [
    'Energy Data',
    'Sunspots'
]

model_choices = [
    'Linear Regression',
    'Support Vector Regression',
    'Random Forest Regression',
    'SARIMAX',
    'SARIMA'
]


################################################################################
############################### FUNCTIONS ######################################
################################################################################


# Creates a log_book and fills it
def create_and_fill_log_book():
    log_book = create_log_book()
    return fill_log_book(log_book)


# This class will create log entries for the purpose of demonstration
def fill_log_book(log_book):
    log_book.append_log_entry(create_log_entry(Log_Entry_Request(dataset_choices[0], 'Linear Regression', 1/2)))
    log_book.append_log_entry(create_log_entry(Log_Entry_Request(dataset_choices[1], 'Linear Regression', 1/2)))
    log_book.append_log_entry(create_log_entry(Log_Entry_Request(dataset_choices[0], 'Linear Regression', 1/2)))
    log_book.append_log_entry(create_log_entry(Log_Entry_Request(dataset_choices[1], 'Linear Regression', 1/2)))
    return log_book


# This class will create log entrie for the purpose of demonstration
def create_log_book():
    log_book = Log_Book()
    return log_book


# Creates a log entry from a log_entry_request and returns it
def create_log_entry(log_entry_request):
    # If dropdown selected is a valid data
    if (log_entry_request.dataset in dataset_choices
        and log_entry_request.model in model_choices
            and log_entry_request.check_valid_ratio()):
        # Create a Log Entry
        log_entry = Log_Entry(log_entry_request.model,
                            log_entry_request.dataset,
                            time.asctime(time.localtime(time.time())),
                            log_entry_request.ratio)
        return log_entry
    else:
        print('log entry could not be created at create_log_entry(log_entry_request)', flush=True)


# Prints the logbook to the console
def print_log_book():
    print('LOGBOOK:')
    for i in range(len(log_book.log_entry_array)):
        print(log_book.log_entry_array[i].dataset, flush=True)


# Updates the logbook buttons being shown on the screen.
def update_log_book_buttons():
    return html.Div(
        children=[
            html.Tr(
                children=[
                    log_book.button_array[i]
                ]
            )
            for i in range(len(log_book.button_array))
        ]
    )

def change_right_hand_side(chosen):
    print('RHS changed to', flush=True)
    if chosen == 'log-entry':
        print('log entry', flush=True)
        return {'display': 'block'}, {'width': '100%', 'display': 'none', 'padding': '0 20'}
    elif chosen == 'log-entry-request':
        print('log entry request', flush=True)
        return {'display': 'none'}, {'width': '100%', 'display': 'block', 'padding': '0 20'}


'''
def return_left_hand_side():
    # If the selected widget is the request forecast widget
    if log_book.selected_button is log_book.request_new_forecast_button:
        return log_entry_request_layout()
    else:
        return log_entry_layout()
'''

################################################################################
############################### HTML LAYOUT ####################################
################################################################################


#Returns the HTML layout for the header
def header_layout():
    return html.Div(
        style={'width': '100%',
                'background-color': colors['white'],
                'color': colors['black']},
        children=[
            # Heading 1
            html.H1(children='Machine Learning Techniques for Time Series Forecasting',
                    style={
                            'display':'block',
                            'text-align':'center',
                            'font-size':35
                },
            ),
            # Heading 2
            html.H2(children='Microsoft Project Group 6',
                style={'text-align': 'center', 'font-size': 15
                },
            )
        ]
    )


# Returns the HTML Layout for logbook
def log_book_layout():
    return html.Div(
        children=[
            html.H2(children='Logbook',
                style={
                    'text-align': 'center',
                    'font-size': 35,
                    'color': colors['black'],
                    'padding': 0
                }
            ),
            html.Div(
                style = {'text-align': 'center'},
                id='request_new_forecast_button',
                children=[log_book.request_new_forecast_button]
            ),
            html.Div(
                    dcc.Dropdown(
                        id='log-book-table',
                        options=[
                            {'label': key, 'value': key} for key in log_entry_dict
                        ],
                        placeholder='Select a Log Entry',
                    ),
            )
        ]
    )


# Returns the HTML layout for log Entry
def log_entry_layout():
    # Update_log_entry_contents(log_book.selected_log_entry)
    return html.Div(
        id = 'log-entry',
        style={'width': '100%', 'height': '1000px', 'display': 'none'},
        children=[

            # Training Data Graph and div
            html.Div(style={'width': '50%','display': 'inline-block'},
                children=[
                    # Title
                    html.H3('Training data graph', style={'text-align': 'center'}),
                    # Graph
                    dcc.Loading(
                        children=[dcc.Graph(style={'width': '100%', 'height': '600px'},
                                            id='training-data-graph')],
                        type='circle',
                    ),
                ]
            ),

            # Forecasting Data Graph
            html.Div(style={'width': '50%', 'display': 'inline-block'},
                children=[
                    # Forecasting data graph
                    html.H3('Forecast data graph', style={'text-align': 'center'}),
                    dcc.Loading(
                        children=[
                            dcc.Graph(style={'width': '100%', 'height': '600px'},
                                        id='forecast-data-graph'),
                        ],
                        type='circle',
                    )
                ]
            ),
        ]
    )


# Returns the HTML layout for the log entry request page
def log_entry_request_layout():
    return html.Div(
        id = 'log-entry-request',
        style = {'display': 'block'},
        children=[
            html.H3('Enter log entry request details',style={'text-align': 'center'}),
            # Dataset dropdown + label div
            html.Div(style={'text-align': 'center', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'width': '40%'},
                children=[
                    html.Label(['Dataset']),
                    dcc.Dropdown(
                        id='Dataset-dropdown',
                        options=[
                            {'label': model, 'value': model} for model in models
                        ],
                        placeholder='Select a Dataset',
                        value=list(model_dict.keys())[0],
                    ),
                ]
            ),

            # Model dropdown label + dropdown div
            html.Div(style={'font-family': 'sans-serif', 'text-align': 'center', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'width': '40%'},
                children=[
                    # Label
                    html.Label(['Model']),
                    # Dropdown
                    dcc.Dropdown(
                        id='Model-dropdown',
                        placeholder='Select a Model',
                        value='None',
                    ),
                ]
            ),
            html.Div(style={'font-family': 'sans-serif', 'text-align': 'center', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'width': '40%'},
            children=[
                html.Label(['Percentage of the data to be used to train the algorithm']),
                html.Div(dcc.Input(id='input-box', type='text')),
                dcc.Loading(
                    children=[
                        html.Button('Submit', id='submit-button'),
                        html.Div(id='output-container-button',
                                children=['Enter a decimal (less than 1 but greater than 0) and press submit'])
                    ]
                )
                ]
            )
        ]
    )


################################################################################
############################### APP LAYOUT #####################################
################################################################################

# Create log book
#log_book = create_and_fill_log_book()
log_book = create_log_book()

# Main layout for the app that calls all the other layout functions
app.layout = html.Div(
    style={'background-color': colors['white'],
            'color': colors['black']},
    children = [
        # Top Bar
        html.Div(
            id="top_bar", children=[header_layout()],
        ),
        # Log book
        html.Div(
            id="log_book", children=[log_book_layout()],
            style={
                'position': 'absolute',
                'width': '20%',
                'left': '0px',
                'display': 'inline-block',
                'background-color': colors['white']
                }
        ),
        # Left hand side of screen (either log entry request page or log entry page)
        html.Div(
            id="left-hand-side",
            children=[log_entry_request_layout(),
                      log_entry_layout()],
            style={ 'position': 'absolute',
                    'width': '80%',
                    'right': '0px',
                    'display': 'block'}
        ),
        html.Div(id='hidden-div', style={'display':'none'}),    
        html.Div(id='hidden-div-2',style ={'display':'none'})
    ]
)


################################################################################
############################### CALLBACKS ######################################
################################################################################


#called if the following change which may require a change in screen.
# 1. the submit button.
# 2. the new request button.
# 3. any log entry button timestamp.
# Returns the new display for log entry and log entry request.
@app.callback([Output('log-entry', 'style'),
                Output('log-entry-request', 'style'),
                Output('training-data-graph', 'figure'),
                Output('forecast-data-graph', 'figure')],
                [Input('log-book-table', 'options'),
                Input('submit-button', 'n_clicks_timestamp'),
                Input('request-new-forecast-button', 'n_clicks_timestamp')]
                + [Input('button' + str(i), 'n_clicks_timestamp') for i in range(len(log_book.button_array))])
def change_LHS(options, submit_timestamp,new_request_timestamp, *button_timestamps):

    button_timestamps_array = list(button_timestamps)

    print('change LHS called')
    print('logs timestamps array =' + str(button_timestamps_array), flush=True)
    print('submit timestamp =' + str(submit_timestamp), flush=True)
    print('new_request timestamp =' + str(new_request_timestamp), flush=True)

    # if trigger is submit timestamp button
    for i in range(len(button_timestamps)):
        if (submit_timestamp > new_request_timestamp and submit_timestamp > button_timestamps_array[i]):
            return ({'display': 'block'},
                    {'width': '100%', 'display': 'none', 'padding': '0 20'},
                    log_book.selected_log_entry.training_graph,
                    log_book.selected_log_entry.forecasting_graph)

    # if trigger is submit new_request button
    for i in range(len(button_timestamps)):
        if (new_request_timestamp > submit_timestamp and new_request_timestamp > button_timestamps_array[i]):
            return ({'display': 'none'},
                    {'width': '100%', 'display': 'block', 'padding': '0 20'},
                    go.Figure(),
                    go.Figure())

    # if trigger is a log entry button
    for i in range(len(button_timestamps)):
        if ( button_timestamps_array[i] > submit_timestamp and button_timestamps_array[i] > new_request_timestamp):
            print('selected button is in button array', flush=True)
            return ({'display': 'block'},
                    {'width': '100%', 'display': 'none', 'padding': '0 20'},
                    log_book.selected_log_entry.training_graph,
                    log_book.selected_log_entry.forecasting_graph)

    if(log_book.selected_button!=log_book.request_new_forecast_button
        and log_book.selected_log_entry != None):
        return ({'display': 'block'},
                {'width': '100%', 'display': 'none', 'padding': '0 20'},
                log_book.selected_log_entry.training_graph,
                log_book.selected_log_entry.forecasting_graph)

    # stops nonetype exception
    return ({'display': 'none'},
            {'width': '100%', 'display': 'block', 'padding': '0 20'},
            go.Figure(),
            go.Figure())


# Called when the submit button is pressed on the log entry request page.
# Returns an updated layout for the log book if the request was valid.
@app.callback(dash.dependencies.Output('hidden-div-2', 'style'),
            [dash.dependencies.Input('submit-button', 'n_clicks')],
            [dash.dependencies.State('Dataset-dropdown', 'value'),
            dash.dependencies.State('Model-dropdown', 'value'),
            dash.dependencies.State('input-box', 'value')])
def submit_log_entry_request(button_value, dataset_dropdown_value,
                            model_dropdown_value, input_box_value ):
    print('submit log entry request()', flush=True)
    # Stops an error message when callback is called during start up.
    if input_box_value is not None :
        print('creating request', flush=True)
        # Create log entry request from input data
        log_entry_request = Log_Entry_Request(dataset_dropdown_value, model_dropdown_value, input_box_value)

        # If the log entry request is valid
        if (log_entry_request.dataset in dataset_choices
            and log_entry_request.model in model_choices
            and log_entry_request.check_valid_ratio()):
            print('log entry request is valid')
            # Create a log entry
            log_entry = create_log_entry(log_entry_request)
            # Add it to the log book
            log_entry_dict[str(log_entry.date) + ' ' + log_entry.dataset] = log_entry
            log_book.append_log_entry(log_entry)
            # Print the log book to the console (for debugging)
            #print_log_book()
            # Update the logbook on the screen
            return update_log_book_buttons()

        else:
            print('***log entry could not be created at submit_log_entry_request()***')
            print('dataset', log_entry_request.dataset,
                    'model', log_entry_request.model,
                    'ratio', log_entry_request.check_valid_ratio())
            # Update the logbook on the screen
            return update_log_book_buttons()

    else:
        print('Request input type was none')
        # Update the logbook on the screen
        return update_log_book_buttons()

@app.callback(
    dash.dependencies.Output('Model-dropdown','options'),
    [dash.dependencies.Input('Dataset-dropdown','value')]
)
def update_model_list(dataset):
    return [{'label': i, 'value': i} for i in model_dict[dataset]]


# Updates the selected button to request new forecast when it is pressed
@app.callback(dash.dependencies.Output('hidden-div', 'style'),
            [dash.dependencies.Input('request-new-forecast-button', 'n_clicks')])
def select_request_new_forecast(n_clicks):
    print('selected button updated to request new forecast')
    print(app.layout['log-book-table'].options)
    log_book.selected_button = log_book.request_new_forecast_button
    return {'display':'none'}

# Updates list of log entries
@app.callback(dash.dependencies.Output('log-book-table','options'),
            [dash.dependencies.Input('submit-button','n_clicks_timestamp')])
def update_log_entries(n_clicks_timestamp):
    return [{'label': i, 'value': i} for i in log_entry_dict]


if __name__ == '__main__':
    app.run_server(debug=True)
