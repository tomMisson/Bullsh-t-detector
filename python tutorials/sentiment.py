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
        # sentence = input()
        # sentence = '''
        '''
        England, who have rested several first-choice players, restricted the Black Caps to what felt like a below-par total, despite dropping five catches, after winning the toss.

        Although the pitch had more pace than the one in the series opener in Christchurch and the square boundaries were short, it never felt like England were in control of the chase.
New Zealand spinners Mitchell Santner and Ish Sodhi were impressive, taking a combined 5-62 from eight overs.

        England in New Zealand - fixtures, results & squads
        Mixed fortunes for England new boys
        After handing debuts to three players in the seven-wicket win on Friday, England gave Lancashire pace bowler Saqib Mahmood his first cap in place of Tom Curran.

        Mahmood, bowling in the powerplay and death overs, finished with 1-46 from four overs.

        Having conceded 15 from his first over, he fought back well in his second by having Tim Seifert caught behind attempting to ramp.

        Mahmood's final two overs, the 17th and 19th of the innings, went for 11 and 15 respectively, although he regularly found the block hole.

        Fellow seamer Pat Brown, who took 1-33 on debut in the series opener, conceded 32 from two overs.

        After not bowling or batting in the first game, Lewis Gregory struck with his first ball in international cricket as he nipped one back to bowl the dangerous Colin de Grandhomme, who made 28 from 12 balls.

        While not new to international cricket, it was only Sam Curran's second T20 international appearance and he was again impressive in taking 2-22.

        England will be disappointed with the quality of their fielding, however. Three of the five dropped catches were fairly routine, with James Vince spilling two simple chances and an extremely tough one.
        '''
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

        # print('Positive: ' + str(float(pos)/len(words)))
        # print('Negative: ' + str(float(neg)/len(words)))

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
# def sentiment(sentence):
    #neg = 0
    #pos = 0
    #neu = 0
    #sentence = sentence.lower()
    #words = sentence.split(' ')
    #for word in words:
    #    classResult = classifier.classify( word_feats(word))
    #    if classResult == 'neg':
    #        neg = neg + 1
    #    if classResult == 'pos':
    #        pos = pos + 1
    #    if classResult == 'neu':
    #        neu = neu + 1

    ##determines the percentage of bias for each type, from the bias per
    ##total word count
    #print('Positive: ' + str(round(((float(pos)/len(words))*100), 1)) + "%")
    #print('Negative: ' + str(round(((float(neg)/len(words))*100), 1)) + "%")
    #print('Neutral: ' + str(round(((float(neu)/len(words))*100), 1)) + "%")

sentence = '''
England, who have rested several first-choice players, restricted the Black Caps to what felt like a below-par total, despite dropping five catches, after winning the toss.

Although the pitch had more pace than the one in the series opener in Christchurch and the square boundaries were short, it never felt like England were in control of the chase.

New Zealand spinners Mitchell Santner and Ish Sodhi were impressive, taking a combined 5-62 from eight overs.

England in New Zealand - fixtures, results & squads
Mixed fortunes for England new boys
After handing debuts to three players in the seven-wicket win on Friday, England gave Lancashire pace bowler Saqib Mahmood his first cap in place of Tom Curran.

Mahmood, bowling in the powerplay and death overs, finished with 1-46 from four overs.

Having conceded 15 from his first over, he fought back well in his second by having Tim Seifert caught behind attempting to ramp.

Mahmood's final two overs, the 17th and 19th of the innings, went for 11 and 15 respectively, although he regularly found the block hole.

Fellow seamer Pat Brown, who took 1-33 on debut in the series opener, conceded 32 from two overs.

After not bowling or batting in the first game, Lewis Gregory struck with his first ball in international cricket as he nipped one back to bowl the dangerous Colin de Grandhomme, who made 28 from 12 balls.

While not new to international cricket, it was only Sam Curran's second T20 international appearance and he was again impressive in taking 2-22.

England will be disappointed with the quality of their fielding, however. Three of the five dropped catches were fairly routine, with James Vince spilling two simple chances and an extremely tough one.
'''


def sentiment(sentence):
#<<<<<<< HEAD
#    neg = 0
#    pos = 0
#    neu = 0
#    sentence = sentence.lower()
#    words = sentence.split(' ')
#    for word in words:
#        classResult = classifier.classify( word_feats(word))
#        if classResult == 'neg':
#            neg = neg + 1
#        if classResult == 'pos':
#            pos = pos + 1
#        if classResult == 'neu':
#            neu = neu + 1

#    #determines the percentage of bias for each type, from the bias per
#    #total word count
#    positive = "positive: " + str(round(((float(pos)/len(words))*100), 1)) + "%"
#    negative = "negative: "+ str(round(((float(neg)/len(words))*100), 1)) + "%"
#    neutral = "neutral: " + str(round(((float(neu)/len(words))*100), 1)) + "%"

#    return (sentence, positive, negative, neutral)

    myClassifier = MyClassifier()
    return (myClassifier.main(sentence))

if __name__ == '__main__':
    app.run(debug=True)

# sentiment(sentence)
