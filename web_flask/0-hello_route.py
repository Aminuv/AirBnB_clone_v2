#!/usr/bin/python3
""" starts A Flask Web Application."""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def Home():
    return "Hello HBNB!"

if __name__ == "__amin__":
    app.run(host="0.0.0.0', post=5000)
