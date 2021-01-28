import os

import Twitter
import Instagram
import Predict
import csv
import random
import sys
import Data_Cleaner
from text import text_processing

def main():
    #check folder
    if not os.path.exists("dataset_instagram"):
        os.makedirs("dataset_instagram")
    if not os.path.exists("dataset_twitter"):
        os.makedirs("dataset_twitter")
    if not os.path.exists("result"):
        os.makedirs("result")

    network = input("Enter the network you want to use (twitter or instagram) : ")
    if network != "twitter" and network != "instagram":
        print("Error of network, please choose between twitter or instagram")
        sys.exit()
    hashtag = input("Enter the hashtag you want to analyse : ")
    if network == "twitter":
        nbtweet = input("Enter the number of tweets you want : ")
    if network == "instagram":
        nbtweet = input("Enter the number of post you want : ")
    language = input("Enter the language you want (en or fr) : ")
    if language != "en" and language != "fr":
        print("Error of language, please choose between en or fr")
        sys.exit()

    if network == "twitter":
        path = Twitter.getTweets(hashtag, int(nbtweet), language)
    elif network == "instagram":
        path = Instagram.get_hash_tag_caption(hashtag, int(nbtweet), "dataset_instagram/"+language+"/"+hashtag+"/"+hashtag+".csv", language)

    if language == "en":
        Data_Cleaner.DataCleanerEn("pred", hashtag, path)
    elif language == "fr":
        Data_Cleaner.DataCleanerFr("pred", hashtag, path)

    pathpred = Predict.predict(network, hashtag, path, language)

    Negative = 0
    Neutral = 0
    Positive = 0
    Total = -1

    with open(pathpred, newline='') as csvfile:
        predfile = csv.reader(csvfile, delimiter=',')
        for row in predfile:
            #Total
            Total = Total + 1
            #Negative
            if row[0] == '0':
                Negative = Negative + 1
            #Neutral
            elif row[0] == '2':
                Neutral = Neutral + 1
            #Positive
            elif row[0] == '4':
                Positive = Positive + 1

    PercentNegative = Negative*100/Total
    PercentNeutral = Neutral*100/Total
    PercentPositive = Positive*100/Total

    print("\nResult for #" + hashtag +" with " + nbtweet + " tweets in " + language + " :")
    print("Negative:", round(PercentNegative, 2), "%")
    print("Neutral:", round(PercentNeutral, 2), "%")
    print("Positive:", round(PercentPositive, 2), "%")

    print("\nRandom examples of prediction :")
    with open(pathpred) as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index == 0:
                chosen_row = row
            else:
                r = random.randint(0, index)
                if r == 0:
                    chosen_row = row
                    print(chosen_row)

if __name__ == "__main__":
    main()