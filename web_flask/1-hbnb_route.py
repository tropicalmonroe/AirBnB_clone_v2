#!/usr/bin/python3
""" Starts flask application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """2 words return"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello2():
    "return word"
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
