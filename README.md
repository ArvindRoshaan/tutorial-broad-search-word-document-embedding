# Implement-a-Broad-Search-Feature-by-Combining-Word-and-Document-Embeddings

**Combine Word2Vec and Doc2Vec embeddings to create an intelligent, broad search capability. The idea is simple:**

**1.** Similar words occur close together.

**2.** Similar documents occur close together.

**3.** In the Doc2Vec DBOW algorithm, by forcing a Word2Vec model to be trained along with the DBOW algorithm, and for relatively smaller sizes of documents (such as in tweets or insurance claim notes), a document containing a word will occur close to the word. 

**4.** So, all documents broadly or partially related to a word will occur close to the word (which is the search query). 

**I used 300 dimensional word and document vectors. The data was about 350k tweets that contained 500 disease-related hashtags collected over ten days using the Twitted Streaming API. The tweets have been phrase collocated.**

**By 'broad' search, I mean the search results will include:**

**1.** Results that don't contain the search term, but is clearly related.

**2.** Results that contain definitions of the search term.

**3.** Results that contain synonyms, subtypes, associated signs, similar terms as the search term.

**Essentially, this can be used as an intelligent alternative to a traditional keyword-based search (which looks for the keywords in the search query). Here, the machine understands the context of the query, and returns results that it thinks are relevant even if they don't contain the search terms!**

This usually works well with large volumes of data (in the millions).

**Modeled in Python**

###Examples:

**Note:** 

**1.** The examples/screenshots below do not show the top results for each search, because the top results all contain the exact search term (which is nothing special). But as we go down (descending cosine similarity), we begin to see tweets that don't contain the search term, but potentially have the same context as the search query. In the examples below, the results are around the 500th 'closest' tweets to the given search term.

**2.** The 'Context Identified' section is for illustrative purposes only, and shows the closest word vectors to the search query. Although it provides us a good idea of what the context might be, the algorithm **does not** prepare such a list and **then** search for the keywords in that list. Rather, it directly finds the closest document vectors to a given word vector. 

![Mosquito](https://github.com/sgrvinod/Implement-a-Broad-Search-Feature-by-Combining-Word-and-Document-Embeddings/blob/master/examples/mosquito.png?raw=true)

![Panic Attacks](https://github.com/sgrvinod/Implement-a-Broad-Search-Feature-by-Combining-Word-and-Document-Embeddings/blob/master/examples/panic%20attacks.png?raw=true)

![Insulin](https://github.com/sgrvinod/Implement-a-Broad-Search-Feature-by-Combining-Word-and-Document-Embeddings/blob/master/examples/insulin.png?raw=true)

![Injury](https://github.com/sgrvinod/Implement-a-Broad-Search-Feature-by-Combining-Word-and-Document-Embeddings/blob/master/examples/injury.png?raw=true)



