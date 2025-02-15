#!/usr/bin/python3
"""Write a script that starts a Flask web application"""


from flask import Flask
from flask import render_template
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


@app.route("/python/", defaults={'text': "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """display "Python" followed by value of text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display "n is a number" only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_tem(n):
    """display HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_eve(n):
    """display HTML page only if n is an integer"""
    if (n % 2) == 0:
        noe = "even"
    else:
        noe = "odd"
    return render_template("6-number_odd_or_even.html", n=n, noe=noe)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
