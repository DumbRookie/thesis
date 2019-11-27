import re
import pandas as pd

tweet_set = set()

with open('/Users/teoflev/Desktop/thesis_code/thesis/tweets/clean_tweets.txt','w') as fout:
    with open('/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweets.txt','r') as fin:
        tweets = fin.readlines()
        for line in tweets:
            line = re.sub("/r", " ", line)
            line = re.sub("/n", " ", line)
            line = re.sub("http", "\n http", line)
            line = re.sub(r"http\S+", "\n", line)
            tweet_set.add(line)
            if line in tweet_set:
                fout.write(line)
    
tweet_frame = pd.read_csv('/Users/teoflev/Desktop/thesis_code/thesis/tweets/clean_tweets.txt', sep=" /n", header=None)
tweet_frame.columns = ['Tweet']

tweet_frame.to_csv(r'/Users/teoflev/Desktop/thesis_code/thesis/tweets/tweet_frame.csv', index = None)
print(tweet_frame)