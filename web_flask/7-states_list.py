#!/usr/bin/python3
""" Module to start a flask web app """
from flask import Flask
from flask import render_template
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def disp_state():
    """ displayn an HTML """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(excep):
    """ Storage.close """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
