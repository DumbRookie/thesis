import pandas as pd

tweet_frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/no_dup_tweets.txt', sep=" /n", header=None)
tweet_frame.columns = ['Tweet']

#tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweet_frame.csv', index = None)
print(tweet_frame)