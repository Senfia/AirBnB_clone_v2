#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application.
Adding more routes
Usage: python3 -m 0-hello_route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def print_c(text):
    """ Prints C followed by a text passed """
    return "C %s" % text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def print_python(text="is cool"):
    """ Prints Python followed by a text passed """
    return "Python %s" % text.replace("_", " ")


@app.route('/number/', strict_slashes=False)
@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """ Prints n followed by a number passed """
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
