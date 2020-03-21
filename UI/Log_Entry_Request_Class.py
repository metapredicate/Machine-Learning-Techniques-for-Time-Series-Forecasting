#object which will contain all the information about the forecast
class log_entry:

    def __init__(self, model, dataset, date):
        self.model = model
        self.dataset = dataset
        self.notes = 'Please write your notes here'
        self.status = 'trainig'
        self.colors = {
            'ready': '#00cc66',
            'trainig': '#ff0000',
            'up': '#00cc66',
            'down': '#ff0000'
            }
        self.data_frame = pd.read_csv(dataset)
        self.metadata = dataframe.describe()
        self.columns = dataframe.columns
        self.training_graph = go.Figure()
        self.forecasting_graph = go.Figure()

    def set_status_to_ready(input):
        self.status = 'ready'

    def set_status_to_training(input):
        self.status = 'training'
