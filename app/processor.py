from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon') # Compute sentiment labels
import pandas as pd
from pandas import DataFrame
from collections import Counter
import os


class Processor:
    def __init__(self, original_data: list[DataFrame]) -> None:
        self.processed_data = self.initialize_processed_data(original_data)
        self.sentimentIntensityAnalyzer = SentimentIntensityAnalyzer()

    def initialize_processed_data(self, original_data):
        """Initialize the processed data with the original data"""
        try:
            processed_data = []
            for doc in original_data:
                temp_df = pd.DataFrame()
                temp_df["id"] = doc["TweetID"]
                temp_df["original_text"] = doc["Text"]
                processed_data.append(temp_df)

            return processed_data
        except Exception as e:
            raise Exception(f"An error occurred while initializing processed data: {e}")


    @staticmethod
    def find_rarest_words(field_vals):
        """find the least appeared word in a given doc field"""
        try:
            return Counter(field_vals).most_common()[-1][0]

        except Exception as e:
            raise Exception(f"An error occurred while finding rarest word: {e}")


    def find_text_emotion(self, field_vals: str):
        """find and returns the emotion of the text in a given doc field"""
        try:
            compound = self.sentimentIntensityAnalyzer.polarity_scores(field_vals).get('compound', 0)
            # Return the emotion based on the compound score
            if compound <= -0.5:
                return 'negative'
            elif -0.50 < compound < 0.5:
                return 'neutral'
            elif compound >= 0.5:
                return 'positive'

        except Exception as e:
            raise Exception(f"An error occurred while finding text emotion: {e}")


    def check_for_weapons_in_text(self, field_vals: str):
        """Check if the given field contains weapons"""
        try:
            weapons = self.load_weapons_data()
            for weapon in weapons:
                if weapon.lower() in field_vals.lower():
                    return weapon

            return ""

        except Exception as e:
            raise Exception(f"An error occurred while checking for weapons in text: {e}")

    @staticmethod
    def load_weapons_data():
        """Load weapons data from a file
        Returns:
            list: A list of weapons if the file is loaded successfully """

        try:
            # Get the directory of the current file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up one level and into data directory
            weapons_file = os.path.join(os.path.dirname(current_dir), 'data', 'weapon_list.txt')
            
            with open(weapons_file, 'r') as f:
                weapons = f.read().splitlines()
                
            # Filter out empty lines and strip whitespace
            weapons = [weapon.strip() for weapon in weapons if weapon.strip()]

            return weapons
        except OSError as e:
            raise Exception(f"Failed to load weapons data: {e}")
        except Exception as e:
            raise Exception(f"Error processing weapons data: {e}")

    def analyze_and_get_processed_data(self):
        """Analyze the data and return the processed data"""
        try:
            if not self.processed_data:
                raise ValueError("No processed data available for analysis")
                
            # count variable to keep track of the DataFrame index
            count = 0
            # Iterate through each DataFrame in the processed_data list
            for df in self.processed_data:
                if df.empty:
                    raise ValueError(f"DataFrame at index {count} is empty")

                # Add a column for the rarest word in each text
                self.processed_data[count]['rarest_word'] = self.processed_data[count]['original_text'].apply(
                    lambda text: self.find_rarest_words([text]) if text and text.strip() else ""
                )

                # Add a column for the emotion of each text
                self.processed_data[count]['emotion'] = self.processed_data[count]['original_text'].apply(
                    lambda text: self.find_text_emotion(text) if text and text.strip() else "neutral"
                )

                # Add a column for weapons found in each text
                self.processed_data[count]['weapons'] = self.processed_data[count]['original_text'].apply(
                    lambda text: self.check_for_weapons_in_text(text) if text and text.strip() else ""
                )

                count += 1

            return self.processed_data

        except Exception as e:
            raise Exception(f"An error occurred while analyzing data: {e}")




