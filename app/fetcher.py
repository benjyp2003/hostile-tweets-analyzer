import os

import pandas as pd
from pymongo import MongoClient, errors
from typing import Any

from app.processor import Processor


class Fetcher:
    CONNECTION_STRING = os.getenv("CONN_STRING", "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
    USERNAME = os.getenv("USERNAME", "IRGC")
    PASSWORD = os.getenv("PASSWORD", "iraniraniran")
    DB_NAME = os.getenv("DB_NAME", "IranMalDB")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "tweets")

    def __init__(self):
        self.conn_string = self.CONNECTION_STRING
        self.client = MongoClient(self.conn_string)
        self.db = self.client[self.DB_NAME]
        self.col = self.db[self.COLLECTION_NAME]

    def fetch_all_docs(self) -> list[dict[str, Any]]:
        """ :returns list of all the docs in the current collection """
        try:
            all_docs = list(self.col.find({}, {"_id": 0}))

            # check if we got any tweets
            if not all_docs:
                print("No tweets found.")
                return []
            return all_docs

        except errors.PyMongoError as e:
            print(f"MongoDB Error: {e}")
            raise Exception(f"Error reading tweets: {e}")


f = Fetcher()
all = f.fetch_all_docs()
count = 0
all =[pd.DataFrame([d]) for d in all]

p = Processor(all)
print((p.analyze_and_get_processed_data()))