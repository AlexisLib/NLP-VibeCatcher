import pandas as pd
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from joblib import dump

train_tweets = pd.read_csv('C:/Users/alexs\Desktop/out.csv')

train_tweets = train_tweets[['label', 'tweet']]

def text_processing(tweet):
    # Generating the list of words in the tweet (hastags and other punctuations removed)
    def form_sentence(tweet):
        tweet_blob = TextBlob(tweet)
        return ' '.join(tweet_blob.words)

    new_tweet = form_sentence(tweet)

    # Removing stopwords and words with unusual symbols
    def no_user_alpha(tweet):
        tweet_list = [ele for ele in tweet.split() if ele != 'user']
        clean_tokens = [t for t in tweet_list if re.match(r'[^\W\d]*$', t)]
        clean_s = ' '.join(clean_tokens)
        clean_mess = [word for word in clean_s.split() if word.lower() not in stopwords.words('english')]
        return clean_mess

    no_punc_tweet = no_user_alpha(new_tweet)

    # Normalizing the words in tweets
    def normalization(tweet_list):
        lem = WordNetLemmatizer()
        normalized_tweet = []
        for word in tweet_list:
            normalized_text = lem.lemmatize(word, 'v')
            normalized_tweet.append(normalized_text)
        return normalized_tweet

    return normalization(no_punc_tweet)

train_tweets['tweet_list'] = train_tweets['tweet'].apply(text_processing)

train_tweets[train_tweets['label'] == 1].drop('tweet', axis=1).head()

X = train_tweets['tweet']
y = train_tweets['label']

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

dump(pipeline, 'model/big-'+acc+'.pkl', compress=1)