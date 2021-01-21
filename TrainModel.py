import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from joblib import dump
from text import text_processing

train_tweets = pd.read_csv('C:/Users/alexs\Desktop/train.csv', sep=',', header=0, encoding='latin-1')

train_tweets = train_tweets[['label', 'tweet']]

train_tweets['tweet_list'] = train_tweets['tweet'].apply(text_processing)

train_tweets[train_tweets['label'] == 1].drop('tweet', axis=1).head()

msg_train, msg_test, label_train, label_test = train_test_split(train_tweets['tweet'], train_tweets['label'], test_size=0.2)

#Machine Learning Pipeline
pipeline = Pipeline([
    ('bow',CountVectorizer(analyzer=text_processing)),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])
pipeline.fit(msg_train, label_train)

predictions = pipeline.predict(msg_test)

print(classification_report(predictions, label_test))
print('\n')
print(confusion_matrix(predictions, label_test))
print(accuracy_score(predictions, label_test))

acc = str(accuracy_score(predictions, label_test))

#Save model
dump(pipeline, 'model/big-v3-'+acc+'.pkl', compress=1)