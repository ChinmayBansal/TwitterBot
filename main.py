import tweepy
import os
from config import api_key, api_secret_key, access_token, access_token_secret

def api():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully')

if __name__ == '__main__':
    api = api()
    tweet(api, 'This was tweeted from python','test.jpeg')