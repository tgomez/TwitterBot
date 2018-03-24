# Dependencies
import tweepy
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

consumer_key = os.environ ['consumer_key']
consumer_secret = os.environ ['consumer_secret']
access_token = os.environ ['access_token']
access_token_secret = os.environ ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

Tweets = [
    "Testing 1",
    "Testing 2"]

for tweet in Tweets:
    api.update_status(tweet)
