from polyglot.text import Text, Word
import pandas as pd
import re
import string
import matplotlib.pyplot as plt
import numpy as np

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

def degree_polarize(item):
    if item == '[]':
        item = 'κενό'

    item = ''.join(ch for ch in item if ch not in punct)
    polarity_counter = 0
    item = Text(item, hint_language_code='el')

    for word in item.words:
        polar = word.polarity
        polarity_counter = polarity_counter + int(polar)

    return (polarity_counter)


tweet_frame['Polarity'] = [polarize(str(item)) for item in tweet_frame.Lemmatized_Tokens]
tweet_frame['Polarity_Intensity'] = [degree_polarize(str(item)) for item in tweet_frame.Lemmatized_Tokens]

tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/polarized_tweet_frame.csv', index = None)

polarity_values = tweet_frame.Polarity_Intensity
values = polarity_values.value_counts()

results = values.as_matrix(columns = None)

neutral_opinion = results[0]
negative_opinion = results[1]
positive_opinion = results[2]

print (values)

#PiePlot
labels = 'Positive', 'Negative'
sizes = [positive_opinion, negative_opinion]
colors = ['green', 'crimson']
explode = (0.01, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
#plt.axis('equal')

"""
#BarPlot
height = [positive_opinion, negative_opinion, neutral_opinion]
bars = ('Positive', 'Negative', 'Neutral')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height)
plt.xticks(y_pos, bars)
"""


plt.show()
