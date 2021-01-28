import pandas as pd

path = input("Enter the path of the CSV you want to labelize : ")
df = pd.read_csv(path, sep=',', header=0, encoding='latin-1')

label = []

for index, row in df.iterrows():
    print(row["tweet"])
    userlabel = input("0 = negative, 2 = neutral, 4 = positive : \n")
    label.append(int(userlabel))

df["label"] = label

df.to_csv('C:/Users/alexs\Desktop/labelized.csv', index=False, header=True)