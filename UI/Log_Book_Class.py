#Object which will contain all the log entries
import dash_html_components as html


class Log_Book:

    # Constructor
    def __init__(self,):
        self.log_entry_array = []
        self.button_array = []
        self.request_new_forecast_button = self.insert_new_request_button()
        self.selected_button = self.request_new_forecast_button
        self.selected_log_entry = None
        print('Log book created', flush=True)

    # Appends a new log entry to the log entry array
    # Appends a new button to the button array which represent the new log entry
    def append_log_entry(self, new_entry):
        self.log_entry_array.append(new_entry)
        self.selected_log_entry = new_entry
        new_button = self.log_entry_to_button(new_entry)
        self.button_array.append(new_button)
        self.selected_button = new_button
        print('New log entry appended to logbook', flush=True)


    # Creates a button to represent a log entry
    def log_entry_to_button(self, new_entry):
        print('New button created', flush=True)
        button_text = str(new_entry.date) + ' ' + new_entry.dataset
        return html.Button(style={'font-size': 'x-small'},
                            id='button' + str(len(self.button_array)),
                            children=[button_text],
                            n_clicks = 0)



    def insert_new_request_button(self):
        print('New button created', flush=True)
        return html.Button(style={'font-size': 'x-small'},
                                    id='request-new-forecast-button',
                                    children=['new-forecast-request'],
                                    n_clicks = 0)
