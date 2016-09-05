import pandas as pd
import numpy as np
import gensim as gen
import string
import nltk
from tkinter import *

# Load doc2vec model into memory
model = gen.models.doc2vec.Doc2Vec.load('C:/Blog/intell/d2v_model_tweets')

# Load dataframe containing labels and text into memory
text = pd.read_csv('C:/Blog/intell/tweets.csv', engine='python')

root = Tk()
label1 = Label(root, text="Search For:")
label1.pack()
ST = Entry(root, bd=5)
ST.pack()


def get_search_results():
    root.update()
    # Input search term
    searchterm = ST.get()

    # Tokenize search term
    searchterm = searchterm.split(" ")

    # Get related terms to individual terms
    similartermslist = []
    for s in searchterm:
        similarterms = pd.DataFrame(model.most_similar(s, topn=30))
        similarterms = similarterms.ix[similarterms[1] > 0.2, :]
        similartermslist.append(similarterms)

    # Create an output string
    similartermsoutput = []
    for i in range(len(similartermslist)):
        similartermsoutput.append(", ".join(list(similartermslist[i][0])))
    similartermsoutput = "\n\n--&--\n\n".join(similartermsoutput)

    # Search results
    # Get word vectors of words in search term
    wordvecs = [model[s] for s in searchterm]
    # Get most similar documents
    similardocs = model.docvecs.most_similar(wordvecs, topn=500)
    similardocs = pd.DataFrame(similardocs)
    similardocs.columns = ['id', 'Similarity']
    similardocs['tweet'] = similardocs['id'].map(lambda x: text['tweet'][text['id'] == x].iloc[0])
    similardocs['Output'] = similardocs[['id', 'tweet']].apply(lambda x: ': '.join(x), axis=1)
    similardocsoutput = ("\n\n").join(list(similardocs['Output']))
    root2 = Tk()
    # Print similar terms
    label1 = Label(root2, text="Context Identified:")
    label1.pack()
    text1 = Text(root2, height=10)
    text1.insert(INSERT, similartermsoutput)
    text1.pack()

    # Print search results
    label1 = Label(root2, text="Tweet Search Results:")
    label1.pack()
    text2 = Text(root2)
    text2.insert(INSERT, similardocsoutput)
    text2.pack()
    root2.mainloop()


submit = Button(root, text="Submit", command=get_search_results)
submit.pack(side=BOTTOM)
root.mainloop()
