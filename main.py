import tweepy
import requests
from config import api_key, api_secret_key, bearer_token, access_token, access_token_secret, quote_key, api_url

client = tweepy.Client(bearer_token, consumer_key=api_key, consumer_secret=api_secret_key,
                       access_token=access_token, access_token_secret=access_token_secret)

def get_quote():
    response = requests.get(api_url, headers={'X-Api-Key': quote_key})
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data:
            item = data[0]
            quote = item['quote']
            author = item['author']
            return quote, author
    return None, None

def attempt_to_tweet(max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        quote, author = get_quote()
        if quote is not None:
            tweet_text = f'"{quote}" - {author}'
            if len(tweet_text) <= 280:
                try:
                    client.create_tweet(text=tweet_text)
                    print(f"Tweeted successfully: {tweet_text}")
                    return
                except tweepy.TweepyException as e:
                    print(f"Failed to tweet: {e}")
                    
            else:
                print(f"Quote is too long ({len(tweet_text)} characters), getting a new one...")
        else:
            print("Failed to get a new quote.")
        attempts += 1
    print("Max tweet attempts reached.")

def main():
    attempt_to_tweet()

if __name__ == "__main__":
    main()
