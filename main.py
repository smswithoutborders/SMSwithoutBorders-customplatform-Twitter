import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def main():
    status = {}

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweet = ""

    n = 280
    result = [''.join(tweet[i:i+n]) for i in range(0,len(tweet),n)]

    if (len(result) > 1):
        status = api.update_status(result[0])
        for i in range(len(result)-1):
            api.update_status('@{}{}'.format(status._json['user']['screen_name'], result[i+1]), '{}'.format(status._json['id']))
            return
    else:
        api.update_status(result[0])
        return
    
if __name__ == "__main__":
    main()