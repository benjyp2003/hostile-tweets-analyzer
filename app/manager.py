import pandas as pd

from app.fetcher import Fetcher
from app.processor import Processor

class Manager:
    def __init__(self):
        self.fetcher = Fetcher()
        self.processor = None
        self.processed_data = []


    def process_data(self):
        try:
            data = self.fetch_data()
            data = self.convert_dicts_to_dataframes(data)
            self.processor = Processor(data)
            processed_data = self.analyze_data()
            processed_data = self.convert_df_to_dict(processed_data)
            self.processed_data = processed_data

        except Exception as e:
            raise Exception(f"Error processing data: {e}")

    def fetch_data(self):
        """ Fetches data from the source. """
        try:
            data = self.fetcher.fetch_all_docs()
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise Exception(f"Error fetching data: {e}")

    def analyze_data(self):
        """ Analyzes the data and returns the processed data. """
        try:
            processed_data = self.processor.analyze_and_get_processed_data()
            return processed_data
        except Exception as e:
            print(f"Error analyzing data: {e}")
            raise Exception(f"Error analyzing data: {e}")


    @staticmethod
    def convert_dicts_to_dataframes(data):
        """
        converts a list of dictionaries to a list of DataFrames.
        """
        try:
            data = [pd.DataFrame([d]) for d in data]
            return data
        except Exception as e:
            print(f"Error converting dict to df: {e}")
            raise Exception(f"Error converting dict to df: {e}")

    @staticmethod
    def convert_df_to_dict(data):
        """
        Converts a list of DataFrames to a list of dictionaries.
        """
        try:
            data = [df.to_dict(orient='records')[0] for df in data]
            return data
        except Exception as e:
            print(f"Error converting df to dict: {e}")
            raise Exception(f"Error converting df to dict: {e}")


    def get_processed_data(self):
        """
        This method returns the processed data.
        """
        return {"processed_data": self.processed_data}