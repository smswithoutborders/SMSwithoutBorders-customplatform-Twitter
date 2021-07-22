#!/usr/bin/python3 

import os
import tweepy
import configparser


# auth=None
def post_tweet(consumer_key, consumer_secret, access_token, access_token_secret, tweet):

    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        tweet_limits = 280
        split_tweets = [''.join(tweet[i:i+tweet_limits]) for i in range(0,len(tweet),tweet_limits)]
        if (len(split_tweets) > 1):
            status = api.update_status(split_tweets[0])
            for i in range(len(split_tweets)-1):
                api.update_status('{}'.format(split_tweets[i+1]), '{}'.format(status._json['id']), True)
        else:
            api.update_status(split_tweets[0])
        return True
    except Exception as error:
        raise Exception(error)

    return False
    
def execute(protocol, body, userDetails):
    print(userDetails)
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '', 'configs.ini'))

    consumer_key = config['AUTH']['key']
    consumer_secret = config['AUTH']['secret']
    print('consumer key', consumer_key)
    print('consumer secret', consumer_secret)

    access_token = userDetails['token']['accToken']
    access_token_secret = userDetails['token']['accTokenSecret']
    print('access token', len(access_token))
    print('access token secret', len(access_token_secret))

    print('acces_token', access_token)
    print(f'acces_token_secret', access_token_secret)

    return post_tweet(consumer_key, consumer_secret, access_token, access_token_secret, body)

    # import traceback

if __name__ == "__main__":
    #post_tweet("Hello world"*300)
    execute('send', "hello world"*300, {"token":{"accToken":sys.argv[1], "accTokenSecret":sys.argv[2]}})
