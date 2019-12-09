from polyglot.text import Text, Word
import pandas as pd
import re
import string

punct = set(string.punctuation)
punct.add('«')
punct.add('»')

tweet_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/tweets/preprocessed_tweet_frame.csv", encoding='utf-8-sig')
 

def polarize(item):
    if item == '[]':
        item = 'κενό'

    item = ''.join(ch for ch in item if ch not in punct)
    polarity_counter = 0
    item = Text(item, hint_language_code='el')

    for word in item.words:
        polar = word.polarity
        polarity_counter = polarity_counter + int(polar)

    if polarity_counter > 0:
        polarity = 1
        return polarity
    elif polarity_counter == 0:
        polarity = 0
        return polarity
    else:
        polarity = -1
        return polarity 


tweet_frame['Polarity'] = [polarize(str(item)) for item in tweet_frame.Lemmatized_Tokens]

print (tweet_frame)
tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/polarized_tweet_frame.csv', index = None)