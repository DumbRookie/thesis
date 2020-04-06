import tweepy 
import json
import numpy as np
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
import time
import keras
import pandas as pd
from gensim.models import Word2Vec
from sklearn.preprocessing import LabelEncoder
import gensim

input = open('/Users/teoflev/Desktop/thesis_code/thesis/tweets/unseen_tweets.txt', "r")


model =  load_model('/Users/teoflev/Desktop/thesis_code/thesis/neural/structured_model.h5')

tokenizer = Tokenizer(num_words=10000)

labels = ['έκπληξη', 'αηδία', 'ανυπομονησία', 'εμπιστοσύνη', 'θλίψη', 'θυμός', 'ουδέτερο', 'φόβος', 'χαρά']
labeled_data = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/training_set_tweets.csv')
w2v = Word2Vec.load("word2vec.model")

sentences = labeled_data['Tweet'].values
emotions = labeled_data['Emotion'].values

encoder = LabelEncoder()
encoder.fit(emotions)
encoded_Y = encoder.fit_transform(emotions)


embedding_dim = 64

#Create new embeddings for unseen words
unseenTweetsList = [gensim.utils.simple_preprocess(tweet) for tweet in input.readlines()]
backup_w2v = Word2Vec(unseenTweetsList, min_count = 1, size = 64, workers= 3, sg=1)


def create_embedding_matrix(text, word_index, embedding_dim):  
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    for word in text:
        try:
            vec = w2v[word.lower()]
        except:
            vec = backup_w2v[word.lower()]
    for word, index in tokenizer.word_index.items():
        if index > vocab_size - 1:
            break
        else: 
            embedding_vector = vec
            if embedding_vector is not None:
                embedding_matrix[index] = embedding_vector
    return embedding_matrix



for line in input.readlines():
    if line != "" or line != "\n":
        tokenizer.fit_on_texts(line)
        vocab_size = len(tokenizer.word_index) + 1   
        emb = create_embedding_matrix(line, tokenizer.word_index, embedding_dim)

        
        prediction = model.predict(emb)
        idxs = np.argsort(prediction)[::-1][:1]

        zipped =  zip(encoder.classes_, prediction)
        sorting = (-prediction).argsort()
        sorted_ = sorting[0][:1]

        for value in sorted_:
            predicted_label = encoder.classes_[value]
        
        print(line + "----> " + predicted_label)
        time.sleep(60)