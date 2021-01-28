import os
import pandas as pd
from joblib import load
from text import text_processing

def predict(network, hashtag, path, language):
    if not os.path.exists("result/"+network):
        os.makedirs("result/"+network)
    if not os.path.exists("result/"+network+"/"+language):
        os.makedirs("result/"+network+"/"+language)

    test_tweets = pd.read_csv(path+"/Cleaned_"+hashtag+".csv", sep=',', header=0, encoding='utf-8')

    test = test_tweets['tweet']

    if language == "en":
        pipeline = load('model/en/big-v4-0.75541875.pkl')
    elif language == "fr":
        pipeline = load('model/fr/big-fr-v1-0.7116720779220779.pkl')

    predictions = pipeline.predict(test)

    output = pd.DataFrame(data={"Prediction":predictions, "tweet":test_tweets["tweet"]})
    output.to_csv(path_or_buf="result/"+network+"/"+language+"/Prediction_"+hashtag+".csv", index=False, quoting=3, sep=',', escapechar='\\')

    pathout = "result/"+network+"/"+language+"/Prediction_"+hashtag+".csv"

    return pathout