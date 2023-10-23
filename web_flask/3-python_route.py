#!/usr/bin/python3
'''
A script that starts a Flask web application.
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_page():
    '''
    Displays a text
    '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
    Displays a text
    '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''
    Displays a text

    Args:
        text (string): the text to be displayed.
    '''
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    '''
    Displays a text

    Args:
        text (string): The text to be displayed.
    '''
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
