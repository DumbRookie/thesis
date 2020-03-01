import pandas as pd
from gensim.models import Word2Vec
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.layers import Dropout
import string
import time


labeled_data = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/training_set_tweets.csv')
model = Word2Vec.load("word2vec.model")

# Vectorization of Words in a sentence

def Sentence2VectorMatrix(sentence):
    sentenceVec = []
    string_sentence = str(sentence)
    words = string_sentence.split(' ')
    try:
        for word in words:
            vec = model[word.lower().translate(str.maketrans('', '', string.punctuation))]
            s = str(vec)
            vector = s[s.find("[")+1:s.find("]")]
            sentenceVec.append(vec)
    except:
        sentenceVec.append(0)

    return sentenceVec



labeled_data['Tweet_Vectors'] = [Sentence2VectorMatrix(line) for line in labeled_data['Tweet']]
indexNames = labeled_data[ labeled_data['Tweet_Vectors'] == 0].index
labeled_data.drop(indexNames , inplace=True)

labeled_data.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/temp.csv', index=None)

