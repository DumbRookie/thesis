from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
from gensim.models import Word2Vec
import numpy as np
import time
import string


def create_embedding_matrix(text, word_index, embedding_dim):
    vocab_size = len(word_index) + 1  
    embedding_list = []

    for line in text:
        for word in line.split():
            try:
                vec = w2v[word.lower().translate(str.maketrans('', '', string.punctuation))]
            except:
                vec = []
            s = str(vec)
            vector = s[s.find("[")+1:s.find("]")]
            print(word)
            print(vector)
            time.sleep(1)
            embedding_list.append(vector)

        embedding_matrix =  np.asarray(embedding_list)
    return embedding_matrix


#Setting up the dataset

labeled_data = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/training_set_tweets.csv')
w2v = Word2Vec.load("word2vec.model")

sentences = labeled_data['Tweet'].values
y = labeled_data['Emotion'].values

sentences_train,sentences_test,y_train,y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(sentences_train)

X_train = tokenizer.texts_to_sequences(sentences_train)
X_test = tokenizer.texts_to_sequences(sentences_test)

vocab_size = len(tokenizer.word_index) + 1                          

maxlen = 100

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

#Creating the word embeddings

embedding_dim = 64
embedding_matrix = create_embedding_matrix(sentences, tokenizer.word_index, embedding_dim)
