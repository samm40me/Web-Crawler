# Web Crawler

## Description

This is a URL crawler writen in Python and supports threads/coroutines.

### Packages Used

    Python 3

    Flask

    Docker 

### Requirements
    Application MUST take the form of a Web API server, providing three endpoints (see next section)
    Application MUST be able to run multiple crawling jobs simultaneously.
    We expect to be able to get information/result about a running/finished job from your application (using its job ID).
    Application should crawl the URLs recursively only until the second level (to avoid a large amount of data). Fetch the images, from img tags, for each given URL and their  children.
    The data extracted will be a set of image URLs (absolute path) for each URL given in the job description, only keep PNG, GIF and JPEG images. There shouldn’t be duplicates in the sets.
    By default, your application will crawl using one thread/coroutine (worker thread/coroutine), however, we should be able to specify the number of thread/coroutine to use when creating a new job.
    Use the JSON format for communication, and follow the messages format defined in the next sections.
    Repository MUST contain a Dockerfile that will be used to build your application.
    Use any technology/library that you want but everything must run in your container.

## Usage

To run virtual environment 

    python -m venv virtual
    source virtual/scripts/activate
    pip freeze - install flask if not on virtual environment
    set flask port to 5000, debug=True and reloader=True

To run the web crawler on docker:

    git clone https://github.com/samm40me/Web-Crawler
    cd your_repo
    docker build -t crawler_test .
    docker run --rm -p 8080:8080 crawler_test:latest

Thought Process 

    A POST message is initated first and return 200. A web crawler can be designed in different ways, in this project, it
    was designed to run the given urls simulatenously, also known as seed websites, to the queue list of the crawler. 
    From the starting websites the crawler collects all hypertext links and adds them into the queue.  
    This means many HTTP requests need to be handled concurrently. After this I invoke crawler with thread. 
    The number of URLs being  processed and completed are shown.The GET method was used lastly to fetch the images. 
 
 Challenges
 
    The main.py (python file) works file and was able to get the images and number of jobs crawed for the docker build -t crawler_test. Hoever, it a bit difficult getting JSON response back from the urls when coupled with flask and executed the run --rm -p 8080:8080 crawler_test:latest. The quick way to fix this would to include a html file through a render_template instead of using postman to view the result. 
