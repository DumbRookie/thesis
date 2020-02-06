from gensim.models import Word2Vec
import gensim
import pandas as pd


training_set = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/training_set_tweets.csv', encoding='utf-8-sig')

tweets = training_set['Lemmatized_Tokens'].values
tweetsVec = [gensim.utils.simple_preprocess(tweet) for tweet in tweets]
CBOW = Word2Vec(tweetsVec, min_count = 1, size = 64, workers= 3, sg=0)
SKIP = Word2Vec(tweetsVec, min_count = 1, size = 64, workers= 3, sg=1)

voc = list(SKIP.wv.vocab)
print(SKIP.most_similar('μετανάστης'))