This repository is the website for GentenStudios and future library for the 
modules created for Genten's projects.

## Community
[Here's a link to our public discord server](https://discord.gg/XRttqAm), where we collaborate and discuss the development of GentenStudios.
[Here's a link to our community guidelines](./CODE_OF_CONDUCT.md)

## Setup
This project is built to run on python 3.8.x

A virtual environment is recommended for use with this project, to set that up
run the following commands:

````
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
````

## Running the project
Once everything is started, launching the web server is super easy:

````
$ export FLASK_APP=app
$ export APP_SETTINGS=config.DevelopmentConfig
$ python run.py
````
