from flask import Flask, render_template  
import flask
from flask import request, jsonify
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from random import randint
import threading
import urllib.request
import logging as logger
from main import *


logger.basicConfig(level="DEBUG")

app = flask.Flask(__name__)

#app.config["DEBUG"] = True


@app.route('/job', methods=['POST'])
def post_request(): 
    return post_request()

#    print("status code = ", post_request()) 

@app.route('/jobs/V1.0/status', methods=['GET'])
def crawler(): 
    return job_counter(SITES)

@app.route('/jobs/V1.0/result', methods=['GET'])
def getdata():
    return getdata()

if __name__ == '__main__':
    logger.debug("Starting Flask Server")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)  