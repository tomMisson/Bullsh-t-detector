# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:41:57 2019

@author: grace
"""
import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

def gender_features(word): 
    return {'last_letter': word[-1]}
 
# Load data and training 
names = ([(name, 'male') for name in names.words('male.txt')] + 
	 [(name, 'female') for name in names.words('female.txt')])

(name, 'male') for name in names.words('male.txt'):
    print(name)
    
featuresets = [(gender_features(n), g) for (n,g) in names]
train_set = featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set) 
 
# Predict
name = input("Name: ")
print(classifier.classify(gender_features(name)))