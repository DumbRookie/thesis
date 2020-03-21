import tweepy 
import json
import numpy as np
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
import time

input = open('/Users/teoflev/Desktop/thesis_code/thesis/tweets/unseen_tweets.txt', "r")


model =  load_model('/Users/teoflev/Desktop/thesis_code/thesis/neural/structured_model.h5')

tokenizer = Tokenizer(num_words=10000)


embedding_dim = 64

def create_embedding_matrix(text, word_index, embedding_dim):  
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    for word in text:
        try:
            vec = w2v[word.lower()]
        except:
            vec = [1]*embedding_dim
    for word, index in tokenizer.word_index.items():
        if index > vocab_size - 1:
            break
        else: 
            embedding_vector = vec
            if embedding_vector is not None:
                embedding_matrix[index] = embedding_vector
    return embedding_matrix



for line in input.readlines():
    tokenizer.fit_on_texts(line)
    vocab_size = len(tokenizer.word_index) + 1   
    emb = create_embedding_matrix(line, tokenizer.word_index, embedding_dim)
    print(emb.shape)
    for word in line.split(' '):
        print(word, emb)
        
    prediction = model.predict([emb])
    print(prediction.shape)
    print(line + "---->" + int(prediction))
    time.sleep(10)