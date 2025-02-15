#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """display "C" followed by value of text variable"""
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
