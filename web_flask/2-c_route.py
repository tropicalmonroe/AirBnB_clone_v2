#!/usr/bin/python3
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """Return two words"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    """Return word"""
    return "HBNB"


@app.route('/c/<path:subpath>', strict_slashes=False)
def route_c(subpath):
    """return subpatth"""
    return "C {}".format(escape(subpath).replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
