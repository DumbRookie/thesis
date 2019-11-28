import re
import pandas

tweet_set = set()

#remove duplicates, after removing URLs
output = open('/Users/teoflev/Desktop/thesis_code/thesis/tweets/clean_data.txt', 'w')
with open('/Users/teoflev/Desktop/thesis_code/thesis/tweets/clean_tweets.txt','r') as tweets:
    while True:
        tweet = tweets.readline()
        if not tweet:
            break
        tweet_set.add(tweet)
        if tweet in tweet_set:
            output.write(tweet)
        
output.close()





