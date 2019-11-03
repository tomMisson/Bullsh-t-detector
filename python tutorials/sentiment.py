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
    return jsonify(sentiment(idNum))
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

class MyClassifier(object):
    def __init__(self):
        pass

    def word_feats(self, words):
        return dict([(word, True) for word in words])

    def main(self, sentence):

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

        positive_features = [(self.word_feats(pos), 'pos') for pos in positive_vocab]
        negative_features = [(self.word_feats(neg), 'neg') for neg in negative_vocab]
        neutral_features = [(self.word_feats(neu), 'neu') for neu in neutral_vocab]

        train_set = negative_features + positive_features + neutral_features
        classifier = NaiveBayesClassifier.train(train_set)

        # Predict
        neg = 0
        pos = 0

        sentence = sentence.lower()
        words = sentence.split(' ')
        for word in words:
            classResult = classifier.classify( self.word_feats(word))
            if classResult == 'neg':
                neg = neg + 1
            if classResult == 'pos':
                pos = pos + 1

        return {"positive": str(float(pos)/len(words)),
                "negative": str(float(neg)/len(words))}

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

def sentiment(sentence):
    myClassifier = MyClassifier()
    return (myClassifier.main(sentence))

if __name__ == '__main__':
    app.run(debug=True)
