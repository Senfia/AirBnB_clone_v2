#!/usr/bin/python3
"""
fetches data from database.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """ displays an HTML page containing list of states """
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
