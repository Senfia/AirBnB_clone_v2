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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ HBNB """
    return "C %s" % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
