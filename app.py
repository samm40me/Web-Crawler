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
    for site in SITES:
        try:
            r = requests.post(site, data=post_json)             
            if r.status_code == 200:                 
                return jsonify(r)
            else:
                return jsonify(r.status_code)
        except Exception as e:             
            return e
    return jsonify({"job-id" : "047500fa-37e3-4a80-a9fe-fdda1e6f1150", "workers": 4,
        "urls": ["https://wolfhumanities.upenn.edu/","https://golang.org/"]})

#    print("status code = ", post_request()) 

def crawler(site):
    if site is None:
        print("Provide a site to crawl")
    else:
        try:
            page = urllib.request.urlopen(site)
            page_size = len(page.read())
            print(f"Home page {site} size is {page_size}")
        except Exception as e:
            print(f"Can't crawl home page on {site}: {e}")

@app.route('/jobs/V1.0/status', methods=['GET'])
def multibot():
    threads = []
    
    for site in SITES:
    	# Invoke crawler with thread
        t = threading.Thread(target=crawler, args=(site,), name=site)
	# Start thread
        t.start()
#        print(f"Starting thread for site {site}")
	# Add thread to list of threads to track status
        threads.append(t)
    
    # Loop over threads until empty
    while threads:
        for thread in threads:
            if thread.is_alive():
                return 'in progress'
            else:
               thread.join()
               return 'completed'
               threads.remove(thread)
           
#multibot(SITES)   
@app.route('/jobs/V1.0/result', methods=['GET'])
def getdata():
    for i in SITES:
	    r = requests.get(i)
	    return r.text 

    htmldata = getdata() 
    soup = bs(htmldata, 'html.parser') 
    for item in soup.find_all('img'):
        for i in SITES:
#        print(item['src'])
            return  {SITES[i]: (item['src'])}       

if __name__ == '__main__':
    logger.debug("Starting Flask Server")
    post_request()
    multibot()
    getdata()  
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)  