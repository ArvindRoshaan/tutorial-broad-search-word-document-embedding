import pandas as pd
from Doc2Vec import DocIterator
import gensim as gen
import re

# Read tweets
tweets = pd.read_csv('C:/Blog/intell/tweets.csv', engine='python')
tweets['tweet']=tweets['tweet'].map(lambda t: re.sub(r'http\S+', '', t))
tweets['tweet']=tweets['tweet'].map(lambda t: re.sub(r'https\S+', '', t))
tweets = tweets.drop_duplicates('tweet')
tweets.shape
tweets.index = range(tweets.shape[0])
tweets['id'] = 'tw' + (tweets.index).astype('str')
# Save this to be read during the intelligent search
tweets.to_csv('C:/Blog/intell/tweets.csv', index=0)

# Create document and label lists
docs = list(tweets['tweet'])
labels = list(tweets['id'])

# Create class instance
d2v = DocIterator(docs, labels)
d2v.checkLabelsUnique()
d2v.prepareDocs()

# Initialize doc2vec model
model = gen.models.Doc2Vec(size=300, window=8, min_count=40, workers=8, alpha=0.025, min_alpha=0.025, dm=0,
                           dbow_words=1)

# Build vocabulary
model.build_vocab(d2v)

# Do model training over several epochs, shuffle documents each time, decrease alpha each time
for epoch in range(10):
    print('Epoch %d of 20.' % (epoch+1))
    d2v.shuffleDocs()
    model.train(d2v)
    model.alpha -= 0.002
    model.min_alpha = model.alpha

# Save model
model.save('C:/Blog/intell/d2v_model_tweets')