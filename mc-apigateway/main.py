from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests

app = Flask(__name__)
cors = CORS(app)
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)
def loadFileConfig():
    with open('config.json') as f:
        data= json.load(f)
        return data
        return data