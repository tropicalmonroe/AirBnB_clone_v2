#!/usr/bin/python3
"""start flask"""
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """2 words"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    """Return a word"""
    return "HBNB"


@app.route('/c/<path:subpath>', strict_slashes=False)
def route_c(subpath):
    """return subpath"""
    return "C {}".format(escape(subpath).replace('_', ' '))


@app.route('/python', defaults={'subpath': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:subpath>', strict_slashes=False)
def route_python(subpath):
    """return the subpath"""
    return "Python {}".format(escape(subpath).replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def route_number(num):
    """return int"""
    return "{} is a number".format(escape(num))


@app.route('/number_template/<int:num>', strict_slashes=False)
def route_template(num):
    """HTML return if int"""
    return render_template("5-number.html", n=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def route_odd_even(num):
    """HTML reurn if num is int describe if odd or even"""
    return render_template("6-number_odd_or_even.html", n=num)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
