import emoji
import pandas as pd 
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string

punct = set(string.punctuation)

tweet_frame = pd.read_csv("/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweet_frame.csv") 

nlp = spacy.load("el_core_news_sm")

def lemmatize(text):
    return [token.lemma_ for token in nlp(text)]

def replace_punctuation(item):
    item = re.sub(r'([a-zA-Z])([,.:_!])', r'\1 \2', item)
    item = ''.join(ch for ch in item if ch not in punct)
    return item
   
# Tokenize tweets
tweet_frame['Token'] = [nlp(text) for text in tweet_frame.Tweet]

# Sum the number of tokens in each Tweet
tweet_frame['num_tokens'] = [len(token) for token in tweet_frame.Token]

# Lemmatization
tweet_frame['Lemmatized_Tokens'] = [lemmatize(tweet) for tweet in tweet_frame.Tweet]

# Removing Emojis
tweet_frame['No_Emoji_Lemma'] = [emoji.demojize(str(lemma)) for lemma in tweet_frame.Lemmatized_Tokens]

# Replacing Punctuation with Whitespace
tweet_frame['No_Punctuation'] = [replace_punctuation(no_e_lemma) for no_e_lemma in tweet_frame.No_Emoji_Lemma]
tweet_frame['No_Punctuation_Lemma'] = [nlp(lemma) for lemma in tweet_frame.No_Punctuation]
tweet_frame = tweet_frame.drop('No_Punctuation', axis = 1)



print (tweet_frame)

tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweet_frame_2.csv', index = None)

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
