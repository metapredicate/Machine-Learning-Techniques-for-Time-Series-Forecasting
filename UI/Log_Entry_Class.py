#object which will contain all the information about the forecast
import pandas as pd
import plotly.graph_objects as go
import math

class Log_Entry:


    #Constructor
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


    #splits the input data_frame into a training_data_frame and
    #forecast_data_frame according to the ratio
    def split_data_frame(self):
        length = len(self.input_data_frame.index)
        self.trainng_data_frame = self.input_data_frame.truncate(before=0, after=math.ceil((length)*self.ratio))
        self.forecast_data_frame = self.input_data_frame.truncate(before=math.ceil((length)*self.ratio), after=length)


    #Sets status of log entry to 'ready'
    def set_status_to_ready(input):
        self.status = 'ready'
        selfstatus_color = '#00cc66'


    #Sets status of log entry to 'training'
    def set_status_to_training(input):
        self.status = 'training'
        self.status_color = '#ff0000'


    #Creates meta_data list
    def generate_meta_data(data_frame):
        self.meta_data = input_data_frame.describe()


    #Adds to meta_data list
    def append_meta_data(new_meta_data):
        self.meta_data.append(new_meta_data)


    #Takes in a log_entry and dataframe so it knows what its trying to graph.
    #Creates a graph and decides which graphing method to call.
    def graph_data(self, data_frame):

        graph = go.Figure()

        if self.dataset == 'energydata_complete.csv':
            graph =self.graph_energydata_complete(graph, data_frame)
        elif self.dataset == 'monthly-sunspots.csv':
            graph = self.graph_monthly_sunspots(graph, data_frame)
        else:
            print('***ERROR***: CANT READ DATA FILE', flush=True)

        return graph


    #Graphs energydata_complete
    def graph_energydata_complete(self, graph, data_frame  ):
        #Add lines
        for x in self.columns:
            if x != 'date':
                if x == 'Energy Usage':
                    graph.add_trace(go.Scatter(x=data_frame.date, y=data_frame[x], name = x, line_color='deepskyblue'))
                else:
                    graph.add_trace(go.Scatter(x=data_frame.date, y=data_frame[x], name = x, line_color='#a6a6a6'))
        #update trace
        graph.add_trace

        #Update range slider
        #dark graph
        graph.update_layout(title_text='Input Data with Rangeslider', xaxis_rangeslider_visible=True, paper_bgcolor='#21252C', plot_bgcolor='#21252C')
        #light graph
        #graph.update_layout( xaxis_rangeslider_visible=True)

        return graph


    #Graphs monthly_sunspots
    def graph_monthly_sunspots(self, graph, data_frame):
        #Add lines
        for x in self.columns:
            if x != 'Month':
                graph.add_trace(go.Scatter(x=data_frame.Month, y=data_frame[x], name = x, line_color='#4db8ff'))
        #update trace
        graph.add_trace
        #Update range slider
        #dark graph
        graph.update_layout(title_text='Forecast Data with Rangeslider', xaxis_rangeslider_visible=True, paper_bgcolor='#21252C', plot_bgcolor='#21252C')
        #light graph
        #graph.update_layout(xaxis_rangeslider_visible=True)
        return graph
