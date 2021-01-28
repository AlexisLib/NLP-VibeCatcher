import gzip

import Predict
import pandas as pd
import Data_Cleaner
import re
import csv

#Predict.predict("insta", "dataset", "en")

Data_Cleaner.DataCleanerEn("pred", "insta", "dataset")

#df = pd.read_csv(r"dataset/nintendo/nintendo.csv", encoding="unicode-escape", header=0)


#df = pd.read_csv("dataset/train/fr/labelized_fr.csv", encoding="utf-8")
#del df['id']
#del df['date']
#df = df.to_csv("dataset/train/fr/labelized_fr.csv", index=False)


pathcheck = 'dataset_instagram/' + language
path = 'dataset_instagram/' + language + '/' + str(name_of_hashtags)

# Check if folder already exist (yes : continue / no : create folder)
if not os.path.exists(pathcheck):
    os.makedirs(pathcheck)
if not os.path.exists(path):
    os.makedirs(path)
