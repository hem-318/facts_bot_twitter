import randfacts
import tweepy
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()
#Accessing credentials from .env file
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
sleep_time = int(os.getenv("sleep_time"))

#Calling twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#where the magic hppns
n=0
while n<1000000000000000000000000000000:

    try:
        x = randfacts.get_fact()
        n = n+1
        print(x)
        tweet = api.update_status(x)
        print ("Number of tweets so far- " , n)
        sleep(sleep_time)
    
    except n==10000000000:
        break
    except StopIteration:
        break

    #Code by @icecracker (github.com/icecrac34r)
