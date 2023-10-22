#!/usr/bin/python3
""" Module to start a flask web app """
from flask import Flask
from flask import render_template
from models.state import State
app = Flask(__name__)


@app.route("/states/<state_id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def disp_states(state_id=None):
    """displays the list of states and the cities"""
    states = storage.all(State)
    if state_id is not None:
        state_id = f'State.{state_id}'
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def tear_down(execpt):
    """ close method """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
