
import pandas as pd 
import spacy
import matplotlib.pyplot as plt
import seaborn as sns

tweet_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweet_frame.csv") 

nlp = spacy.load("el_core_news_sm")

#tokenize tweets
tweet_frame['Token'] = [nlp(text) for text in tweet_frame.Tweet]

# Sum the number of tokens in each Tweet
tweet_frame['num_tokens'] = [len(token) for token in tweet_frame.Token]


print (tweet_frame)

"""
# Visualize histogram of tokens per tweet
g = sns.distplot(tweet_frame.num_tokens)
sns.despine(left=True, bottom=True)
plt.xlabel('Number of Tokens')
plt.ylabel('Number of Tweets')
plt.title('Number of Tokens per Tweet', fontsize=20)
plt.tick_params(axis='x', which='major', labelsize=9)
plt.show()

"""







