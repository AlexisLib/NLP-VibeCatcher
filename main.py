import Tweeter
import Predict
import csv
import random
import sys
import Data_Cleaner
from text import text_processing

def main():
    hashtag = input("Enter a hashtag to start to start the sentiment analysis : ")
    nbtweet = input("Enter the amount of tweets you want : ")
    language = input("Enter the language you want (en or fr) : ")
    if language != "en" and language != "fr":
        print("Error of language, please choose between en or fr")
        sys.exit()

    path = Tweeter.getTweets(hashtag, int(nbtweet), language)

    if language == "en":
        Data_Cleaner.DataCleanerEn("pred", hashtag, path)
    elif language == "fr":
        Data_Cleaner.DataCleanerFr("pred", hashtag, path)

    pathpred = Predict.predict(hashtag, path, language)

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