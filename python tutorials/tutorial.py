# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:21:40 2019

@author: grace
"""
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer

#some generic text 
data = "All work and no play makes jack a dull boy, all work and no play"
#a list of common words like 'the' and 'a' to be omitted
stopWords = set(stopwords.words('english'))
#create me a list of all the words in the data set
words = word_tokenize(data)
#separate the semntances
phrases = sent_tokenize(data)
#empty set time
wordsFiltered = []

#for each word in the sentance
for w in words:
    # if that word is not a stop word
    if w not in stopWords:
        #add it to the list
        wordsFiltered.append(w)

#print the words
print(words)
#print the phrases
print(phrases)
#print the filtered list
print(wordsFiltered)
#print the stop words for reference
print(stopWords)

# As an example, test the word stem function on different forms of the word 'game'
words = ["game","gaming","gamed","games"]
# A popular function to determine stem words
ps = PorterStemmer()
 
#for every word in the sentance
for word in words:
    #determine the stem word (useful for comparison)
    print(ps.stem(word))


#for an example sentance 
sentence = "gaming, the gamers play games"
#break down the data into words
words = word_tokenize(sentence)

#then determine the stem of each word 
for word in words:
    print(word + ":" + ps.stem(word))

#for a new example
document = 'Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.'
#create an empty set
data = []
#create a list of sentances
sentences = sent_tokenize(document)   
for sent in sentences:
    #compare these codes to the table given on https://pythonspot.com/category/nltk/
    print(nltk.pos_tag(word_tokenize(sent)))
    #add to data the tag
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))

for word in data: 
    if 'NNP' in word[1]: 
        print(word)