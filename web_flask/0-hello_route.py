#!/usr/bin/python3
""" A srcipt that starts Flask Web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, HBNB!"
