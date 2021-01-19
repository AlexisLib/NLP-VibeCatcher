import Tweeter
import TrainModel
import Predict

def main():
    hashtag = input("Enter a hashtag to start to start the sentiment analysis : ")
    Tweeter.getTweets(hashtag)

if __name__ == "__main__":
    main()