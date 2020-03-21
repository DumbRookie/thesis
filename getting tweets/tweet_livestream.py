import tweepy 
import json

consumer_key = "njNVdAoRQgJf3y6HZZQNBx6a4"
consumer_secret = "1KOFRo0qcyIL0ri1XH0I0GGpnpd88opviAAeThIe1GAR3Abi2i"
access_token = "3109593947-lMcGABIJyFtetMjFDE1kPVGhOi49TYUn86wMU0D"
access_token_secret = "nM2AcPv3Mu02SxOjavbtY0H9ydSBw4mT8CLqAUTddM4hQ"




with open('/Users/teoflev/Desktop/thesis_code/thesis/tweets/unseen_tweets.txt', 'a') as output:
    class Listener(tweepy.StreamListener):

        def on_status(self, status):
            if hasattr(status, "retweeted_status"):  # Check if Retweet
                try:
                    s = status.retweeted_status.extended_tweet["full_text"]
                    
                    appendage = status.retweeted_status.extended_tweet["full_text"]
                    
                except AttributeError:
                    s = status.retweeted_status.text
                    
                    appendage = status.retweeted_status.text
            else:
                try:
                    s = status.extended_tweet["full_text"]
                    
                    appendage = status.extended_tweet["full_text"]
                except AttributeError:
                    s =status.text 
                    
                    appendage = status.text
            #output.write(appendage)
            print(s) 

        def on_error(self, status_code):
            if status_code == 420:
                return False
    
    class Stream():
        def __init__(self, auth, listener):
            self.stream = tweepy.Stream(auth = auth, listener = listener)

        def start(self):
            self.stream.filter(track=['μετανάστης', 'μετανάστρια', 'μετανάστευση', 'μεταναστευτικό',
                'πρόσφυγας', 'προσφυγικό', 'λαθρομετανάστης', 'προσφυγόπουλα'])

    if __name__ == '__main__':
        listener = Listener()

    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    stream = Stream(auth, listener)
    stream.start()
    
    