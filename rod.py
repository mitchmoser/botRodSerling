#!/usr/bin/env python3
import markovify
import tweepy

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tp = tweepy.API(auth)

# get raw text as string
with open("rod.txt", encoding="utf-8") as f:
    text = f.read()

# build model
text_model = markovify.Text(text)

# markovify sentence + hashtag (toghether = 140 characters)
tweet = text_model.make_short_sentence(127) + "\n#TwilightZone"

# send to twitter
tp.update_status(tweet)
