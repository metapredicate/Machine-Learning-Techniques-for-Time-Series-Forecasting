#object which will contain all the log entries
import dash_html_components as html

class Log_Book:

    def __init__(self,):
        self.log_entry_array = []
        self.button_array = []
        self.selected_log_entry = 'none'
        print('Log book created', flush=True)

    def append_log_entry(self, new_entry):
        self.log_entry_array.append(new_entry)
        self.button_array.append(self.log_entry_to_button(new_entry))
        print('New log entry appended to logbook', flush=True)

    def log_entry_to_button(self, new_entry):
        print('New button created', flush=True)
        return html.Button(new_entry.dataset)
