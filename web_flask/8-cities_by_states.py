#!/usr/bin/python3
"""
fetches data from database.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_list', strict_slashes=False)
def display_cities():
    """ displays an HTML page containing cities of states """
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
