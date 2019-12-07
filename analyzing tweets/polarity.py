from polyglot.text import Text
import pandas as pd

tweet_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/tweets/preprocessed_tweet_frame.csv") 

pol = Text("I love this hatred")

print (pol)