from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
from gensim.models import Word2Vec
import numpy as np
import time
import string
from keras.models import Sequential
from keras import layers
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
from sklearn.preprocessing import LabelEncoder


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


embedding_dim = 64

#Setting up the dataset
#y = to_categorical(emotions, num_classes=len(list(emotions)))
labeled_data = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/training_set_tweets.csv')
w2v = Word2Vec.load("word2vec.model")

sentences = labeled_data['Tweet'].values
emotions = labeled_data['Emotion'].values

encoder = LabelEncoder()
encoder.fit(emotions)
encoded_Y = encoder.transform(emotions)
y = to_categorical(encoded_Y)


sentences_train,sentences_test,y_train,y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(sentences_train)

X_train = tokenizer.texts_to_sequences(sentences_train)
X_test = tokenizer.texts_to_sequences(sentences_test)

vocab_size = len(tokenizer.word_index) + 1                          

maxlen = 64

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

#Creating the word embeddings
embedding_matrix = create_embedding_matrix(tokenizer.word_docs.keys(), tokenizer.word_index, embedding_dim)

# Creating the neural network

model = Sequential()
model.add(layers.Embedding(vocab_size, embedding_dim, input_length=maxlen, weights= [embedding_matrix]))
model.add(layers.Conv1D(128, 5, activation='relu'))
model.add(layers.GlobalMaxPooling1D())
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(9, activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
history = model.fit(X_train, y_train,
                    epochs=10,
                    validation_data=(X_test, y_test),
                    batch_size=10)

loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
print("Training Accuracy: {:.4f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
print("Testing Accuracy:  {:.4f}".format(accuracy))
#plot_history(history)

# serialize model to JSON
model_json = model.to_json()
with open("/Users/teoflev/Desktop/thesis_code/thesis/neural/model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("/Users/teoflev/Desktop/thesis_code/thesis/neural/model_weights.h5")
model.save("/Users/teoflev/Desktop/thesis_code/thesis/neural/structured_model.h5")