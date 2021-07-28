# Hatchways back-end challenge

## Prerequisite
- Install python 3.9.1
- (recommended) after copying the folders and files within a directory, create  virtual environment by typing `python3 -m venv env`. Activate the environnement by typing `source env/bin/activate`

## Install command
install the python packages : `pip3 install -r requirements.txt`

## Run command
To start the back-end: `uvicorn src.main:app`. the port used is 8000
To run all unitest: `python3 -m unittest discover -p '*_test.py'`