import pandas as pd
from pandas import DataFrame
from collections import Counter

class Processor:
    def __init__(self, data: DataFrame):
        self.data = data
        self.processed_data = {}

    def find_rarest_words(self, field: str):
        """find the least appeared word in a given doc field"""
        try:
            # check that the data in the field is a string
            if type(self.data[field]) != str:
                print("Field values must be a string")
                return None

            # count how many times each word appears
            words_counter = dict(Counter(" ".join(self.data[field]).split()))
            if len(words_counter) == 0:
                print("No words found")
                return None

            # find the min number of appeared words
            least_appeared_words_counter = min(list(words_counter.values()))

            # find the first word from all the rarest words
            first_rarest_word = [word for word, count in words_counter.items() if count == least_appeared_words_counter][0]
            return first_rarest_word
        
        except Exception as e:
            print(f"An error accord while finding rarest word: ", e)
            return None

data = {
    'id': [12345],
    'Text': [1123456789]
}

df = pd.DataFrame(data)
p = Processor(df)
print(p.find_rarest_words("Text"))