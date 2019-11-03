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
        pos.append(lines[1])
    elif (lines[1] == "neutral"):
        nut.append(lines[1])
    elif (lines[1] == "negative"):
        neg.append(lines[1])


positive_vocab = positive
negative_vocab = negative
neutral_vocab = neutral
 
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

train_set = negative_features + positive_features + neutral_features
classifier = NaiveBayesClassifier.train(train_set)

# Predict
neg = 0
pos = 0
sentence = input()
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
    classResult = classifier.classify( word_feats(word))
    if classResult == 'neg':
        neg = neg + 1
    if classResult == 'pos':
        pos = pos + 1
 
print('Positive: ' + str(float(pos)/len(words)))
print('Negative: ' + str(float(neg)/len(words)))