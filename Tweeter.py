import tweepy
import csv

def getTweets(hashtag):
    consumer_key = 'BlAhYK7FLy0TLVwJ4Yos0CDjT'
    consumer_secret = 's7RHZV4R777MixWYUnszNM6jV6OAUh3L2NPJfGMmNqrIygi5hx'
    access_token = '2848499321-1dyNlM3cjKFQtvyuLcuKBokgB9xWdhYwoQl9LHu'
    access_token_secret = 'l98NfSUyHdbNROoUaUnocPQeImxlnOlhszZa33RFfMYlH'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    csvFile = open('C:/Users/alexs/PycharmProjects/VibeCatcher/data/'+hashtag+'.csv', 'a')
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search, q=hashtag, count=100, lang="en", since="2017-04-03").items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

