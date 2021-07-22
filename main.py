#!/usr/bin/python3 

import tweepy
import configparser

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__), '', 'configs.ini')

auth=None
consumer_key = config['AUTH']['key']
consumer_secret = config['AUTH']['secret']

def post_tweet(tweet):
    api = tweepy.API(auth)
    tweet_limits = 280
    split_tweets = [''.join(tweet[i:i+tweet_limits]) for i in range(0,len(tweet),tweet_limits)]
    # print(result)

    if (len(split_tweets) > 1):
        status = api.update_status(split_tweets[0])
        for i in range(len(result)-1):
            api.update_status('{}'.format(result[i+1]), '{}'.format(status._json['id']), True)
    else:
        api.update_status(split_tweets[0])
        return
    
def execute(protocol, body, userDetails):
    access_token = userDetails['access_token']
    access_token_secret = userDetails['acces_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

if __name__ == "__main__":
    post_tweet("Hello world"*300)
