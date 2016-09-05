# Implement-a-Broad-Search-Feature-by-Combining-Word-and-Document-Embeddings
Combine Word2Vec and Doc2Vec embeddings to create an intelligent, broad search capability. The idea is simple:
1. Similar words occur close together.
2. Similar documents occur close together.
3. In the Doc2Vec DBOW algorithm, by forcing a Word2Vec model to be trained along with the DBOW algorithm, and for relatively smaller sizes of documents (such as in tweets or insurance claim notes), a document containing a word will occur close to the word. 
4. So, all documents broadly or partially related to a word will occur close to the word (which is thesearch query). 

I used 300 dimensional word and document vectors. The data was about 350k tweets that contained 500 disease-related hashtags collected over ten days using the Twitted Streaming API.

By 'broad' search, I mean the search results will include:
1. Results that don't contain the search term, but is clearly related.
2. Results that contain definitions of the search term.
3. Results that contain synonyms, subtypes, associated signs, similar terms of the search term.

This usually works well with large volumes of data (in the millions).

**Modeled in Python**

Note: The examples/screenshots below do not show the top results for each search, because the top results all contain the exact search term (which is nothing special). But as we go down (descending cosine similarity), we begin to see tweets that don't contain the search term, but are still valid results.


