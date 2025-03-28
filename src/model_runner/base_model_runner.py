import pandas as pd


class BaseModelRunner:

    def __init__(self, csv_data_path: str):
        self.csv_data_path: str = csv_data_path
        self.df: pd.DataFrame = None

    def load_data(self) -> None:
        """
        Method used to pull the data from the CSV file and transform it into
        a DataFrame
        """

        self.df = pd.read_csv(self.csv_data_path)

    def preprocess(self):
        """
        Method used to preprocess the data and do Feature Engineering
        """
        raise NotImplementedError("This method has not be implemented yet.")
