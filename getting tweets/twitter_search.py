import tweepy 

consumer_key = "njNVdAoRQgJf3y6HZZQNBx6a4"
consumer_secret = "1KOFRo0qcyIL0ri1XH0I0GGpnpd88opviAAeThIe1GAR3Abi2i"
access_token = "3109593947-lMcGABIJyFtetMjFDE1kPVGhOi49TYUn86wMU0D"
access_token_secret = "nM2AcPv3Mu02SxOjavbtY0H9ydSBw4mT8CLqAUTddM4hQ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

query = 'πρόσφυγας'
new_q = query + "-filter:retweets"

language = "el"
twpp = 300
results = api.search(q = new_q, lang = language, rpp = twpp, tweet_mode = 'extended')

for text in results:
    print (text.full_text)

