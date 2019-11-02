#comment


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
def getUrl(idNum=-1):
    for item in url_list:
        if int(item["id"]) == int(idNum):
            return jsonify(item)
    abort(404)

@app.route("/url/", methods=["GET"])
def getAllUrl():
    return jsonify(url_list)

@app.route("/url", methods=["POST"])
def postUrl():
    if not request.json or not 'url' in request.json:
        abort(400)
    url = {
            "id" : len(url_list),
            "url":request.json['url']
            }
    url_list.append(url)
    return jsonify({'url': url}), 201

if __name__ == '__main__':
    app.run(debug=True)
