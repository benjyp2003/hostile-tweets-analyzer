from typing import Any
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')# Compute sentiment labels
import pandas as pd
from pandas import DataFrame
from collections import Counter


class Processor:
    def __init__(self, original_data: list[DataFrame]) -> None:
        self.processed_data = self.initialize_processed_data(original_data)


    def initialize_processed_data(self, original_data):
        """Initialize the processed data with the original data"""
        processed_data = []
        for doc in original_data:
            temp_df = pd.DataFrame()
            temp_df["id"] = doc["TweetID"]
            temp_df["original_text"] = doc["Text"]
            processed_data.append(temp_df)

        return processed_data


    @staticmethod
    def find_rarest_words(field_vals):
        """find the least appeared word in a given doc field"""
        try:
            # count how many times each word appears
            words_counter = dict(Counter(" ".join(field_vals).split()))
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


    def find_text_emotion(self, field_vals: str):
        """find and returns the emotion of the text in a given doc field"""
        try:
            score = SentimentIntensityAnalyzer().polarity_scores(field_vals)
            compound = score['compound']
            # Return the emotion based on the compound score
            if compound <= -0.5:
                return 'negative'
            elif -0.50 < compound < 0.5:
                return 'neutral'
            elif compound >= 0.5:
                return  'positive'

        except Exception as e:
            print(f"An error occurred while finding text emotion: ", e)
            return None


    def check_for_weapons_in_text(self, field_vals: str):
        """Check if the given field contains weapons"""
        try:
            weapons = self.load_weapons_data()
            for weapon in weapons:
                if  weapon in field_vals:
                    return weapon

            return ""

        except Exception as e:
            print(f"An error occurred while checking for weapons in text: ", e)
            return None

    @staticmethod
    def load_weapons_data():
        """Load weapons data from a file
        Returns:
            list: A list of weapons if the file is loaded successfully, None otherwise """

        try:
            with open('..\data\weapon_list.txt', 'r') as f:
                weapons = f.read().splitlines()
            if not weapons:
                print("No weapons found in the file")
                return None
            return weapons
        except OSError as e:
            print(f"Failed to load weapons data: {e}")
            return None

    def analyze_and_get_processed_data(self):
        """Analyze the data and return the processed data"""
        try:
            # count variable to keep track of the DataFrame index
            count = 0
            # Iterate through each DataFrame in the processed_data list
            for df in self.processed_data:

                # Add a column for the rarest word in each text
                self.processed_data[count]['rarest_word'] = self.processed_data[count]['original_text'].apply(lambda text: self.find_rarest_words([text]))

                # Add a column for the emotion of each text
                self.processed_data[count]['emotion'] = self.processed_data[count]['original_text'].apply(lambda text: self.find_text_emotion(text))

                # Add a column for weapons found in each text
                self.processed_data[count]['weapons'] = self.processed_data[count]['original_text'].apply(lambda text: self.check_for_weapons_in_text(text))

                count += 1

            return self.processed_data

        except Exception as e:
            print(f"An error occurred while analyzing data: ", e)
            return None




