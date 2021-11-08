import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from random import randint
import threading
import urllib.request

post_json = {"urls": ["https://wolfhumanities.upenn.edu/","https://golang.org/"],
"workers": 4
}

SITES = post_json['urls']
data = post_json.pop('urls')


def post_request(): 
    for site in SITES:
        try:
            r = requests.post(site, data=post_json)             
            if r.status_code == 200:                 
                return r.json()
            else:
                print(r.status_code)
        except Exception as e:             
            print(e)


print("status code = ", post_request()) 

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

def job_counter(sites):
    threads = []
    
    for site in sites:
    	# Invoke crawler with thread
        t = threading.Thread(target=crawler, args=(site,), name=site)
	# Start thread
        t.start()
        print(f"Starting thread for site {site}")
	# Add thread to list of threads to track status
        threads.append(t)
    
    # Loop over threads until empty
    while threads:
        for thread in threads:
            if thread.is_alive():
               print(f"Thread {thread.name} in progress...")
            else:
               thread.join()
               print(f"Thread {thread.name} completed.")
	       # Remove from thread list, since it's now finished
               threads.remove(thread)
job_counter(SITES)   

def getdata():
    for i in SITES:
	    r = requests.get(i)
	    return r.text 

htmldata = getdata() 
soup = bs(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    print(item['src'])
