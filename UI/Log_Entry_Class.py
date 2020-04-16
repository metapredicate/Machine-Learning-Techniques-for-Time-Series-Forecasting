import pandas as pd
import plotly.graph_objects as go
import math
import pathlib


# Object which will contain all the information about the forecast
class Log_Entry:


    # Constructor
    def __init__(self, model, dataset, date, ratio):
        self.model = model
        self.dataset = dataset
        self.date = date
        self.ratio = ratio
        self.notes = 'Please write your notes here'
        self.status = 'training'
        self.status_color = '#ff0000'
        if(dataset == 'Energy Data'):
            p = pathlib.Path('../Data/Appliances Energy Usage Prediction/energydata_complete.csv')
            self.input_data_frame = pd.read_csv(p)
        else:
            p = pathlib.Path('../Demonstrations/monthly-sunspots.csv')
            self.input_data_frame = pd.read_csv(p)
        self.training_data_frame = self.input_data_frame
        self.forecast_data_frame = self.input_data_frame
        self.split_data_frame()
        self.meta_data = self.input_data_frame.describe()
        self.columns = self.input_data_frame.columns
        self.training_graph = self.graph_data(self.training_data_frame)
        self.forecasting_graph = self.graph_data(self.forecast_data_frame)
        print('Log Entry Created',flush=True)


    # Splits the input data_frame into a training_data_frame and
    # Forecast_data_frame according to the ratio
    def split_data_frame(self):
        length = len(self.input_data_frame.index)
        self.training_data_frame = self.input_data_frame.truncate(before=0, after=math.ceil((length)*self.ratio))
        self.forecast_data_frame = self.input_data_frame.truncate(before=math.ceil((length)*self.ratio), after=length)


    # Sets status of log entry to 'ready'
    def set_status_to_ready(self, input):
        self.status = 'ready'
        self.status_color = '#00cc66'


    # Sets status of log entry to 'training'
    def set_status_to_training(self, input):
        self.status = 'training'
        self.status_color = '#ff0000'


    # Creates meta_data list
    def generate_meta_data(self, data_frame):
        self.meta_data = self.input_data_frame.describe()


    # Adds to meta_data list
    def append_meta_data(self, new_meta_data):
        self.meta_data.append(new_meta_data)


    # Takes in a log_entry and dataframe so it knows what its trying to graph.
    # Creates a graph and decides which graphing method to call.
    def graph_data(self, data_frame):

        graph = go.Figure()

        if self.dataset == 'Energy Data':
            graph =self.graph_energydata_complete(graph, data_frame)
        elif self.dataset == 'Sunspots':
            graph = self.graph_monthly_sunspots(graph, data_frame)
        else:
            print('***ERROR***: CANT READ DATA FILE', flush=True)

        return graph


    # Graphs energydata_complete
    def graph_energydata_complete(self, graph, data_frame  ):
        # Add lines
        for x in self.columns:
            if x != 'date':
                if x == 'Appliances':
                    graph.add_trace(go.Scatter(x=data_frame.date, y=data_frame[x], name = x, line_color='deepskyblue'))
                elif x == 'Forecast':
                    graph.add_trace(go.Scatter(x=data_frame.Month, y=data_frame[x], name=x, line_color='#fc4136'))
                else:
                    graph.add_trace(go.Scatter(x=data_frame.date, y=data_frame[x], name = x, line_color='#a6a6a6'))
        # Update trace
        graph.add_trace
        # Update range slider
        # Dark graph
        # graph.update_layout(title_text='Input Data with Rangeslider', xaxis_rangeslider_visible=True, paper_bgcolor='#21252C', plot_bgcolor='#21252C')
        # Light graph
        graph.update_layout( xaxis_rangeslider_visible=True)

        return graph


    # Graphs monthly_sunspots
    def graph_monthly_sunspots(self, graph, data_frame):
        # Add lines
        for x in self.columns:
            if x != 'Month':
                if x == 'Forecast':
                    graph.add_trace(go.Scatter(x=data_frame.Month, y=data_frame[x], name=x, line_color='#fc4136'))
                else:
                    graph.add_trace(go.Scatter(x=data_frame.Month, y=data_frame[x], name=x, line_color='#4db8ff'))

        # Update trace
        graph.add_trace
        # Update range slider
        # Dark graph
        #graph.update_layout(title_text='Forecast Data with Rangeslider', xaxis_rangeslider_visible=True, paper_bgcolor='#21252C', plot_bgcolor='#21252C')
        # Light graph
        graph.update_layout(xaxis_rangeslider_visible=True)
        return graph


    '''
    # Calls the appropriate forecasting methods
    # Each method gets the training data passed to it
    # Each method returns the forecast
    def call_forecasting_methods(self):
        if self.model == 'Linear Regression':
            self.forecast_data_frame = linear_regression_function(self.training_data_frame)
        if self.model == 'Support Vector Regression':
            self.forecast_data_frame = suport_vector_function(self.training_data_frame)
        if self.model == 'Random Forest Regression':
            self.forecast_data_frame = random_forest_function(self.training_data_frame)
        if self.model == 'Logistic Regression':
            self.forecast_data_frame = logistic_regression_function(self.training_data_frame)
        if self.model == 'SARIMA':
            self.forecast_data_frame = sarima_function(self.training_data_frame)
        if self.model == 'SARIMAX':
            self.forecast_data_frame = sarimax_function(self.training_data_frame)
        return
    '''
