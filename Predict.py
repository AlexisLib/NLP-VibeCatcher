import pandas as pd
from joblib import load
from text import text_processing

def predict(hashtag, path):
    test_tweets = pd.read_csv(path, sep=',', header=0, encoding='latin-1')

    test_tweets['tweet_list'] = test_tweets['tweet'].apply(text_processing)

    test = test_tweets['tweet']

    pipeline = load('model/big-v3-0.760462355513902.pkl')

    predictions = pipeline.predict(test)

    output = pd.DataFrame(data={"Prediction":predictions, "date":test_tweets["date"], "tweet":test_tweets["tweet"]})
    output.to_csv(path_or_buf="result/Prediction_"+hashtag+".csv", index=False, quoting=3, sep=',', escapechar='\\')

    pathout = "result/Prediction_"+hashtag+".csv"

    return pathout