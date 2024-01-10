# Chat Application

**Team Members:** Abhinav Venkatesh, Dhrumil Makwana, Maaz Afzal Shaikh, Sana Fathima, Shaily Preetham Kurra, Sri Nikitha Kalidindi

Production Deployment link for chat application: [Chat App](http://35.224.20.5:3000/)

**Architecture Diagram:** [Architecture](https://github.com/maazshaik/chat_app/blob/main/Architecture%20Diagram.pdf)

## A Level work description

- **Web application -** Developed using React, Node JS and Python
- **Basic form, reporting -** Through web pages for user login, registration, user home and message  
- **Data collection -** User Credentials, Friend details and Messages are collected from the user 
- **Data analyzer -** Analysis of messages for expletive content
- **Unit tests -** Performed using unittest module in python
- **Data persistence -** Using Redis, PostgreSQL databases
- **Data store -** User Credentials, Friend details, Messages are stored
- **Rest collaboration internal or API endpoint -** REST endpoint between front-end and backend
- **Product environment -** GKE cluster

- **Integration tests -** Performed between different components like database instance, front-end, back-end and analyzer
- **Using mock objects or any test doubles -** Used fakeredis module in python to mock the functionality of Redis
- **Continuous integration -** Achieved using GitHub Actions
- **Production monitoring instrumenting -** Using /dbstatus endpoint [/dbstatus](https://github.com/maazshaik/chat_app/wiki/Monitoring-DB-status)

- **Acceptance tests -** Performed by Gopala Krishna Vasanth Kanugo (Acceptance Tests.xlsx)
- **Event collaboration messaging -** Using RabbitMQ to analyze messages for expletive content
- **Continuous delivery -** Achieved using GitHub Actions


## References:
* https://flask.palletsprojects.com/en/2.0.x/
* https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
* https://devcenter.heroku.com/articles/getting-started-with-python

# ChatApp 

## Overview

ChatApp is a simple chat application developed in Python, featuring a Flask-based backend. It leverages Redis for real-time messaging and utilizes various utility functions for configuration and database management.

## Features

- **Friend Management:** Add and manage friends with the `/friend/add` endpoint.
- **Database Status:** Retrieve the database status using the `/dbstatus` endpoint.
- **Friend List:** Obtain the list of friends with the `/friends` endpoint.
- **Messaging:** Send and receive messages through the `/send` endpoint.
- **User Creation:** Create new users using the `/createuser` endpoint.

## Requirements

- Flask
- Gunicorn
- Flask-Heroku
- Redis
- Fakeredis

## Configuration

- Modify the `Configuration.py` file for any configuration-related settings, such as Redis connection details.

## Endpoints

1. **Add Friend:**
   - **Endpoint:** `/friend/add`
   - **Method:** POST

2. **Database Status:**
   - **Endpoint:** `/dbstatus`
   - **Method:** GET

3. **Friend List:**
   - **Endpoint:** `/friends`
   - **Method:** GET

4. **Send/Receive Message:**
   - **Endpoint:** `/send`
   - **Method:** POST, GET

5. **Create User:**
   - **Endpoint:** `/createuser`
   - **Method:** POST

## Running the dev environment:

There are a total of 3 processes. 

Terminal 1
```
yarn install
yarn startboth
```

Terminal 2
```
cd chat-server
python3 app.py
```

Terminal 3
```
cd analyzer
python3 analyzer.py
```

---
