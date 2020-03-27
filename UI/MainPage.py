import time
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from Log_Book_Class import Log_Book
from Log_Entry_Class import Log_Entry
from Log_Entry_Request_Class import Log_Entry_Request
from dash.dependencies import Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


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
    'Data\Appliances Energy Usage Prediction\energydata_complete.csv',
    'Demonstrations\monthly-sunspots.csv'
]

model_choices = [
    'Linear Regression'
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
                id='request_new_forecast_button',
                children=[log_book.request_new_forecast_button]
            ),
            html.Table(
                id='log-book-table',
                children=[],
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
            html.Div(style={'width': '50%', 'display': 'inline-block', 'padding': '5'},
                children=[
                    html.Label(['Dataset']),
                    dcc.Dropdown(
                        id='Dataset-dropdown',
                        options=[
                            {'label': 'Energy Data', 'value': dataset_choices[0]},
                            {'label': 'Sunspots', 'value': dataset_choices[1]}
                        ],
                        placeholder='Select a Dataset',
                        value='None',
                    ),
                ]
            ),

            # Model dropdown label + dropdown div
            html.Div(style={'width': '50%', 'display': 'inline-block', 'padding': '5'},
                children=[
                    # Label
                    html.Label(['Model']),
                    # Dropdown
                    dcc.Dropdown(
                        id='Model-dropdown',
                        options=[
                            {'label': 'Linear Regression', 'value': model_choices[0]},
                        ],
                        placeholder='Select a Model',
                        value='None',
                    ),
                ]
            ),
            html.Div([
                html.Label(['Dataset']),
                html.Div(dcc.Input(id='input-box', type='text')),
                dcc.Loading(
                    children=[
                        html.Button('Submit', id='button'),
                        html.Div(id='output-container-button',
                                children=['Enter a bottom heavy fraction or a decimal ' +
                                        'less than one but greater than 0 and press submit'])
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
        )
    ]
)


################################################################################
############################### CALLBACKS ######################################
################################################################################


# Called when the submit button is pressed on the log entry request page.
# Returns an updated layout for the log book if the request was valid.
@app.callback([dash.dependencies.Output('log-book-table', 'children'),
            dash.dependencies.Output('log-entry', 'style'),
            dash.dependencies.Output('log-entry-request', 'style'),
            dash.dependencies.Output('training-data-graph', 'figure'),
            dash.dependencies.Output('forecast-data-graph', 'figure')],
            [dash.dependencies.Input('button', 'n_clicks')],
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
            log_book.append_log_entry(log_entry)
            # Print the log book to the console (for debugging)
            print_log_book()
            # Update the logbook on the screen
            #Display_log_entry_contents(log_entry)
            return update_log_book_buttons(), {'display': 'block'},  {'width': '100%', 'display': 'none', 'padding': '0 20'}, log_book.selected_log_entry.training_graph, log_book.selected_log_entry.forecasting_graph

        else:
            print('***log entry could not be created at submit_log_entry_request()***')
            print('dataset', log_entry_request.dataset,
                    'model', log_entry_request.model,
                    'ratio', log_entry_request.check_valid_ratio())
            # Update the logbook on the screen
            return update_log_book_buttons(), {'display': 'none'},  {'width': '100%', 'display': 'block', 'padding': '0 20'}, go.Figure(), go.Figure()

    else:
        print('Request input type was none')
        # Update the logbook on the screen
        return update_log_book_buttons(), {'display': 'none'},  {'width': '100%', 'display': 'block', 'padding': '0 20'}, go.Figure(), go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)
