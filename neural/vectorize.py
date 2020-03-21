from gensim.models import Word2Vec
import gensim
import pandas as pd
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.preprocessing.text import Tokenizer

import numpy as np
import math
from collections import defaultdict



training_set = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/training_set_tweets.csv', encoding='utf-8-sig')

tweets = training_set['Tweet'].values
emotions = training_set['Emotion'].values

tweetsVec = [gensim.utils.simple_preprocess(tweet) for tweet in tweets]
emotionVec = [gensim.utils.simple_preprocess(emotion) for emotion in emotions]

CBOW = Word2Vec(tweetsVec, min_count = 1, size = 64, workers= 3, sg=0)
SKIP = Word2Vec(tweetsVec, min_count = 1, size = 64, workers= 3, sg=1)

emCBOW = Word2Vec(emotionVec, min_count = 1, size = 64, workers= 3, sg=0)
emSKIP = Word2Vec(emotionVec, min_count = 1, size = 64, workers= 3, sg=1)

voc = list(SKIP.wv.vocab)

SKIP.save("word2vec.model")
print (SKIP.wv.vocab)
"""

list_of_tweets = []
for tweet in tweets:
    list_of_tweets.append(tweet)
    
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(list_of_tweets)
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)

col_list = list(df.columns)
eng_names =[]
for col in col_list:
    if str(col).isascii():
        eng_names.append(col)

df = df[df.columns.drop(eng_names)]
print(df['γαλλία'])
df.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/resources/tfidf.csv', index= None)

"""
"""
for item in voc:
    print(len(list(SKIP[item])), item)
    time.sleep(0.5)
"""
