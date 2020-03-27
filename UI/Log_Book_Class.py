import dash_html_components as html


# Object which will contain all the log entries
class Log_Book:


    # Constructor
    def __init__(self,):
        self.log_entry_array = []
        self.button_array = []
        self.request_new_forecast_button = self.insert_new_request_button()
        self.selected_button = self.log_button_array[0] if len(self.log_entry_array)>0 else self.request_new_forecast_button
        self.selected_log_entry = None 
        print('Log book created', flush=True)


    # Appends a new log entry to the log entry array
    # Appends a new button to the button array which represent the new log entry
    def append_log_entry(self, new_entry):
        self.log_entry_array.append(new_entry)
        self.selected_button = self.log_entry_to_button(new_entry)
        self.button_array.append(self.log_entry_to_button(new_entry))
        self.selected_log_entry = new_entry
        print('New log entry appended to logbook', flush=True)


    # Creates a button to represent a log entry
    def log_entry_to_button(self, new_entry):
        print('New button created', flush=True)
        button_text = str(new_entry.date) + ' ' + new_entry.dataset
        return html.Button(children = button_text)


    # Creates and returns the "new request button"
    def insert_new_request_button(self):
        return html.Button( id = 'request-new-forecast-button',
                            children = 'request new forecast')
