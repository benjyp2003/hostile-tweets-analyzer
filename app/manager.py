import pandas as pd

from fetcher import Fetcher
from processor import Processor

class Manager:
    def __init__(self):
        self.processed_data = []


    def process_data(self):
        try:
            fetcher = Fetcher()
            data = fetcher.fetch_all_docs()

            # Convert each dictionary in the list to a DataFrame
            data = [pd.DataFrame([d]) for d in data]
            processor = Processor(data)
            processed_data = processor.analyze_and_get_processed_data()
            processed_data = [doc.to_dict(orient='records')[0] for doc in processed_data]
            self.processed_data = processed_data

        except Exception as e:
            return {"error": str(e)}


    def get_processed_data(self):
        """
        This method returns the processed data.
        """
        return {"processed_data": self.processed_data}