import tweepy
import csv


def getTweets(hashtag):
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    csvFile = open('C:/Users/alexs/PycharmProjects/VibeCatcher/data/'+hashtag+'.csv', 'a')
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search, q=hashtag, count=100, lang="en", since="2017-04-03").items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

