# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:46:11 2019

@author: grace
"""
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names

#################################################
# stuff from main.py for flask backend          #
#################################################

from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource, reqparse
import random
import time

app = Flask(__name__)

url_list = [
        {
            "id" : 0,
            "url" : "https://www.bbc.co.uk/news/uk-politics-50275383"
            }
]

@app.route("/")
def helloWorld():
    return "Hello World\n"

@app.route("/url/<idNum>", methods=["GET"])
def getUrl(idNum):
    # return jsonify(idNum)
    # returnThing = sentiment(idNum)

    return jsonify(sentiment(idNum))
    # for item in url_list:
        # if int(item["id"]) == int(idNum):
            # return jsonify(item)
    abort(404)

@app.route("/url/", methods=["GET"])
def getAllUrl():
    return jsonify(url_list)

@app.route("/url", methods=["POST"])
def postUrl():
    if not request.json or not 'url' in request.json:
        abort(400)
    # url = {
            # "id" : len(url_list),
            # "url":request.json['url']
            # }
    url = {
            "id" : len(url_list),
            "text" : request.json['url']
            }
    url_list.append(url)

    return jsonify({'url': sentiment(url)}), 201

#################################################

def word_feats(words):
    return dict([(word, True) for word in words])

f = open("../Dataset.txt", "r")

positive=[]
negative=[]
neutral=[]

for line in f:
    line = line.split(' ')
    line[1] = line[1].replace("\n", '')


    if(line[1]=="positive"):
        positive.append(line[0])
    elif (line[1] == "neutral"):
        neutral.append(line[0])
    elif (line[1] == "negative"):
        negative.append(line[0])


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
    positive = "positive: " + str(round(((float(pos)/len(words))*100), 1)) + "%"
    negative = "negative: "+ str(round(((float(neg)/len(words))*100), 1)) + "%"
    neutral = "neutral: " + str(round(((float(neu)/len(words))*100), 1)) + "%"

    return (sentence, positive, negative, neutral)

if __name__ == '__main__':
    app.run(debug=True)
