#!/usr/bin/python3 

import tweepy
import math
import textwrap

def post_tweet(access_token, tweet):
    try:
        client = tweepy.Client(access_token)

        # max length of tweet
        tweet_max = 280
        # obtain length of tweet
        tweet_length = len(tweet)

        # check length
        if tweet_length <= tweet_max:
            client.create_tweet(text=tweet, user_auth=False)
            return True

        elif tweet_length >= tweet_max:
            # divided tweet_length / 280
            # You might consider adjusting this down 
            # depending on how you want to format the 
            # tweet.
            tweet_length_limit = tweet_length / 280

            # determine the number of tweets 
            # math.ceil is used because we need to round up
            tweet_chunk_length = tweet_length / math.ceil(tweet_length_limit)

            # chunk the tweet into individual pieces
            tweet_chunks = textwrap.wrap(tweet, math.ceil(tweet_chunk_length), break_long_words=False)

            tweet_id = None
            # iterate over the chunks 
            print("\nSending tweet ...")
            for x, chunk in zip(range(len(tweet_chunks)), tweet_chunks):
                if x == 0:
                    # send first tweet and get the tweet_id
                    first_tweet = client.create_tweet(text=chunk, user_auth=False)
                    tweet_id = first_tweet.data["id"]
                else:
                    # send subsequent tweets in reply to the previous tweet_id
                    n_tweet = client.create_tweet(text=chunk, in_reply_to_tweet_id=tweet_id, user_auth=False)
                    tweet_id = n_tweet.data["id"]

            print("\nSent")
            return True
                
    except tweepy.TweepyException as error:
        print(error)
    except Exception as error:
        print(error)

# protocol = send -> str
# body = tweet text -> str
# userDetails = user token -> dict
def execute(protocol, body, userDetails):
    print(userDetails)

    access_token = userDetails['access_token']
    print(f"access token = {access_token}")

    return post_tweet(access_token=access_token, tweet=body)

if __name__ == "__main__":
    # Place token object here 
    token = {}

    #post_tweet("Hello world"*300)
    execute('send', "hello world"*300, token)

