# Web Crawler

## Description

This is a URL crawler writen in Python and supports threads/coroutines.

### Packages Used

    Python 3

    Flask

    Docker 

### Requirements
    Application MUST take the form of a Web API server, providing three endpoints (see next section)
●   Application MUST be able to run multiple crawling jobs simultaneously.
● We expect to be able to get information/result about a running/finished job from your application (using its job ID).
● Your application should crawl the URLs recursively only until the second level (to avoid a large amount of data). Fetch the images, from img tags, for each given URL and their children.
● The data extracted will be a set of image URLs (absolute path) for each URL given in the job description, only keep PNG, GIF and JPEG images. There shouldn’t be duplicates in the sets.
● By default, your application will crawl using one thread/coroutine (worker thread/coroutine), however, we should be able to specify the number of thread/coroutine to use when creating a new job.
● You MUST use the JSON format for communication, and follow the messages format defined in the next sections.
● Your repository MUST contain a Dockerfile that will be used to build your application.
● You can use any technology/library that you want but everything must run in your container.

## Usage

To use and setup the python script and expand into a working, responsive web application, continuously deployed in AWS Cloud:

To connect to Ubuntu Server:

    log into aws ec2 console and create an ec2 instance with SSH and HTTP security group
    
    download keypairs to configure putty and connect to the Ubuntu Serser

To run python and GNU Screen on Ubuntu Server:

    sudo apt-get update
    sudo apt install python3-pip
    sudo apt install python3-regex
    sudo apt-get install screen

To run the web crawler on docker:

    git clone https://github.com/samm40me/Web-Crawler
    cd your_repo
    docker build -t crawler_test .
    docker run --rm -p 8080:8080 crawler_test:latest

Thought Process 

    A POST message is initated first and return 200 if the job_id exist. A web crawler can be designed in different ways. In this project it
    was designed to add a few starting websites, also known as seed websites, to the queue list of the crawler. From the starting websites the crawler collects all hypertext         links and adds them into the queue.  This means many HTTP requests need to be handled concurrently. After this we invoke crawler with thread. The number of URLs being           processed and completed are shown.The GET method used lastly to fetch     the images. It is usually challenge to put a POST and GET methods in the same code, but we were         able to achieve this creating functions and using different variables. 
