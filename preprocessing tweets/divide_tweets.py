import re
with open('/Users/teoflev/Desktop/thesis_code/tweets/out_tweets.txt','w') as fout:
    with open('/Users/teoflev/Desktop/thesis_code/tweets/tweets.txt','r') as fin:
        tweets = fin.readlines()
        for line in tweets:
            line = re.sub("/r", " ", line)
            line = re.sub("/n", " ", line)
            line = re.sub("http", "\n http", line)
            fout.write(line)