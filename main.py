import tweepy
import requests
import json
from config import api_key, api_secret_key,bearer_token, access_token, access_token_secret, quote_key, api_url


client = tweepy.Client(bearer_token,api_key, api_secret_key, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
api = tweepy.API(auth)


response = requests.get(api_url, headers={'X-Api-Key': quote_key})

if response.status_code == requests.codes.ok:
    print(response.text)
    data = response.json()
    item = data[0]
    quote = item['quote']
    author = item['author']
    print(quote)
    print(author)
    tweet_text = f'"{quote}" - {author}'
    client.create_tweet(text = tweet_text)
else:
    print("Error:", response.status_code, response.text)


