#!/usr/bin/python3
""" Module to start a flask web app """
from flask import Flask
from flask import render_template
from models.state import State
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def index():
    """ display an HTML Page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states,
                            amenities=amenities)


@app.tear_down_appcontext
def tear_down(excep):
    """ close method """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
