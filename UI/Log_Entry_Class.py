import pandas as pd
import plotly.graph_objects as go
import math


# Object which will contain all the information about the forecast
class Log_Entry:


    # Constructor
    def __init__(self, model, dataset, date, ratio ):
        self.model = model
        self.dataset = dataset
        self.date = date
        self.ratio = ratio
        self.notes = 'Please write your notes here'
        self.status = 'training'
        self.status_color = '#ff0000'
        self.input_data_frame = pd.read_csv(dataset)
        self.trainng_data_frame = self.input_data_frame
        self.forecast_data_frame = self.input_data_frame
        self.split_data_frame()
        self.meta_data = self.input_data_frame.describe()
        self.columns = self.input_data_frame.columns
        self.training_graph = self.graph_data(self.trainng_data_frame)
        self.forecasting_graph = self.graph_data(self.forecast_data_frame)
        print('Log Entry Created',flush=True)


    # Splits the input data_frame into a training_data_frame and
    # Forecast_data_frame according to the ratio
    def split_data_frame(self):
        length = len(self.input_data_frame.index)
        self.trainng_data_frame = self.input_data_frame.truncate(before=0, after=math.ceil((length)*self.ratio))
        self.forecast_data_frame = self.input_data_frame.truncate(before=math.ceil((length)*self.ratio), after=length)


    # Sets status of log entry to 'ready'
    def set_status_to_ready(self,input):
        self.status = 'ready'
        self.status_color = '#00cc66'


    # Sets status of log entry to 'training'
    def set_status_to_training(self,input):
        self.status = 'training'
        self.status_color = '#ff0000'


    # Creates meta_data list
    def generate_meta_data(self,input_data_frame):
        self.meta_data = input_data_frame.describe()


    # Adds to meta_data list
    def append_meta_data(self,new_meta_data):
        self.meta_data.append(new_meta_data)


    # Takes in a log_entry and dataframe so it knows what its trying to graph.
    # Creates a graph and decides which graphing method to call.
    def graph_data(self, data_frame):

        graph = go.Figure()

        if self.dataset == 'Data\Appliances Energy Usage Prediction\energydata_complete.csv':
            graph =self.graph_energydata_complete(graph, data_frame)
        elif self.dataset == 'Demonstrations\monthly-sunspots.csv':
            graph = self.graph_monthly_sunspots(graph, data_frame)
        else:
            print('***ERROR***: CANT READ DATA FILE', flush=True)

        return graph


    # Graphs energydata_complete
    def graph_energydata_complete(self, graph, data_frame  ):
        # Add lines
        for x in self.columns:
            if x != 'date':
                if x == 'Energy Usage':
                    graph.add_trace(go.Scatter(x=data_frame.date, y=data_frame[x], name = x, line_color='deepskyblue'))
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
                graph.add_trace(go.Scatter(x=data_frame.Month, y=data_frame[x], name = x, line_color='#4db8ff'))
        # Update trace
        graph.add_trace
        # Update range slider
        # Dark graph
        #graph.update_layout(title_text='Forecast Data with Rangeslider', xaxis_rangeslider_visible=True, paper_bgcolor='#21252C', plot_bgcolor='#21252C')
        # Light graph
        graph.update_layout(xaxis_rangeslider_visible=True)
        return graph
