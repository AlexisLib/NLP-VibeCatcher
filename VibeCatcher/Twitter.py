import tweepy
import csv
import os
from datetime import date

def getTweets(hashtag, nbtweet, language):
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    today = date.today()

    pathcheck = 'dataset_twitter/'+language
    path = 'dataset_twitter/'+language+'/'+str(hashtag)

    # Check if folder already exist (yes : continue / no : create folder)
    if not os.path.exists(pathcheck):
        os.makedirs(pathcheck)
    if not os.path.exists(path):
        os.makedirs(path)

    f = open(path+'/'+hashtag+'.csv', "w")
    writer = csv.DictWriter(f, fieldnames=["date", "tweet"], lineterminator='\n')
    writer.writeheader()
    f.close()

    csvFile = open(path+'/'+hashtag+'.csv', 'a')
    csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')

    for tweet in tweepy.Cursor(api.search, q=hashtag, count=100, lang=language, since=today).items(nbtweet):
        #print(tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

    return path
