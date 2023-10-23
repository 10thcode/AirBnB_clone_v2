#!/usr/bin/python3
"""
Define a module to serve requests for
states.
"""
from models.state import State
from models import storage
from os import environ
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list")
def states_list():
    """ Retrieve a list of all states. """
    states = storage.all(State)

    return (render_template("7-states_list.html",
            states=states))


@app.route("/cities_by_states")
def cities_by_states():
    """ Retrieve a list of cities by states. """
    states = storage.all(State)

    return (render_template("8-cities_by_states.html",
            states=states))


@app.teardown_appcontext
def destroy(obj):
    storage.close()


if __name__ == "__main__":
    app.run(host="0")
