[![Build Status](https://travis-ci.org/xcixor/ireporter-api.svg?branch=develop)](https://travis-ci.org/xcixor/ireporter-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/b3a31de2211223ae5f15/maintainability)](https://codeclimate.com/github/xcixor/ireporter-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/xcixor/ireporter-api/badge.svg)](https://coveralls.io/github/xcixor/ireporter-api)
## iReporter
iReporter is an a whistle blowing application that enables people to raise concerns about issues that are affecting them to the authorities.
## Motivation
Poor services in the private and public sector, increasing national debt and poor leadership have derailed the progress of this country. iReporter provides a platform for citizens to take part in the improvement of this situation.

## Built with
- Flask

## Installation
=> This setup assumes you are using a unix based OS
### Step #1
- Create the directory where you want to clone the repository. For this purpose I shall use ireporter
- move into that directory and clone the repository as shown below
-     mkdir ireporter
-     cd ireporter/
-     git clone https://github.com/xcixor/iReporter.git
### Step #2 create a virtual environment and install the requirements
- python3 -m venv ireporter
- source ireporter/bin/activate (to activate virtual env)
- pip install -r requirements.txt (install app dependencies)
### Step #3: Set up Postgres locally on your machine and create a database
You can install Postgres for ubuntu 16.04 [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04) or for mac [here](https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d). Create a Postgres user and password and create a database.

### Step #4 set up .env variables
- Some data is required by the application to run. This includes database setup and as the data varies from
  development environment to the other, its placed on the .env file. The variables are set as below.
    - create the .env file
    - open the file in the editor add the following information
        - export HOST="localhost"
        - export POSTRGRESPORT="5432"
        - export DATABASE_NAME=the db to use during development
        - export USER=the user of the password
        - export PASSWORD=password of postgres user
    - run the following command to activate the environment variables
        -       source .env
### Step #5 start the app
To start the app run the command below
-     python run.py
## Testing
- To test the app run the command below
-     py.test --cov=app test/ (to test and give coverage)