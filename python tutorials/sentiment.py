# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:46:11 2019

@author: grace
"""
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

def word_feats(words):
    return dict([(word, True) for word in words])

f = open("../dataset.tff", "r")

neededLines = []
positive=[]
negative=[]
neutral=[]
n=0

for line in f:
    line = line.split(' ')
   

    if (line[4] == "stemmed1=y" or line[3]=="pos1=noun"):
        n+=1
        neededLines.append(line[2]+"="+line[5])
    
    else:
        next

for lines in neededLines:
    lines = lines.split('=')
    lines = lines[1] + " " + lines[3].replace("\n", '')

    lines = lines.split(" ")

    if(lines[1]=="positive"):
        positive.append(lines[1])
    elif (lines[1] == "neutral"):
        neutral.append(lines[1])
    elif (lines[1] == "negative"):
        negative.append(lines[1])


positive_vocab = positive
negative_vocab = negative
neutral_vocab = neutral
 
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

train_set = negative_features + positive_features + neutral_features
classifier = NaiveBayesClassifier.train(train_set)

# Predict
def sentiment(sentence):
    neg = 0
    pos = 0
    neu = 0
    sentence = sentence.lower()
    words = sentence.split(' ')
    for word in words:
        classResult = classifier.classify( word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1
        if classResult == 'neu':
            neu = neu + 1
    
    #determines the percentage of bias for each type, from the bias per 
    #total word count
    print('Positive: ' + str(round(((float(pos)/len(words))*100), 1)) + "%")
    print('Negative: ' + str(round(((float(neg)/len(words))*100), 1)) + "%")
    print('Neutral: ' + str(round(((float(neu)/len(words))*100), 1)) + "%")