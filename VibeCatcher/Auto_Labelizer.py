import re
import sys
import pandas as pd

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

language = input("Enter the language of your dataset (en or fr) : ")
if language == "en":
    negative_words_file = 'dict/en/negative_words_en.txt'
    positive_words_file = 'dict/en/positive_words_en.txt'
elif language == "fr":
    negative_words_file = 'dict/fr/negative_words_fr.txt'
    positive_words_file = 'dict/fr/positive_words_fr.txt'
else:
    print("Error with the language")
    sys.exit()

path = input("Enter the path of the CSV you want to labelize : ")
df = pd.read_csv(path, sep=',', header=0, encoding='latin-1')

label = []

for index, row in df.iterrows():
    neg = 0
    pos = 0

    with open(negative_words_file) as f:
        for line in f:
            if findWholeWord(line[:-1])(row["tweet"]):
                neg = neg + 1

    with open(positive_words_file) as f:
        for line in f:
            if findWholeWord(line[:-1])(row["tweet"]):
                pos = pos + 1

    if neg > pos:
        #Negative
        label.append(0)
    elif pos > neg:
        #Positive
        label.append(4)
    else:
        #Neutral
        label.append(2)

df["label"] = label

df.to_csv('dataset/labelized.csv', index=False, header=True)