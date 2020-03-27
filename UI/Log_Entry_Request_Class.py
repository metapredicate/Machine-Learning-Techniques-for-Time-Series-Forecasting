# Object which will contain all the information about the forecast
class Log_Entry_Request:


    # Constructor
    def __init__(self, dataset, model, ratio):
        self.model = model
        self.dataset = dataset
        self.ratio = ratio


    # Checks if the ratio the user entered is valid
    def check_valid_ratio(self):
        self.ratio = float(self.ratio)
        # If valid ratio
        if self.ratio>0 and self.ratio<1:
            return self.ratio
        else:
            return None
