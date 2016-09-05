import json
import os
import pandas as pd

directories = os.listdir('C:/Blog/intell/May Twitter Data')

data = []
for d in directories:
    files = os.listdir('C:/Blog/intell/May Twitter Data/' + d)
    print(d)
    for f in files:
        with open('C:/Blog/intell/May Twitter Data/' + d + '/' + f) as fi:
            for lineno, line in enumerate(fi):
                try:
                    data.append(json.loads(line))
                except Exception:
                    pass
tweets = []
for i in range(len(data)):
    if len(data[i]) > 1:
        tweets.append(data[i]['text'])

df = pd.DataFrame({'tweet': pd.Series(tweets)})

df['id'] = 'Tw' + (df.index).astype('str')

df = df.drop_duplicates('tweet')

df.to_csv('C:/Blog/intell/tweets.csv', header=1, index=0, encoding='utf-8')
