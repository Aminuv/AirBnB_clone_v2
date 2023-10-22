#!/usr/bin/python3
""" Module to start a flask web app """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Home():
    """ display Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """ C is called """
    return "C " + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ display doc paythone """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def disp_num(n):
    """ desplay the doc number """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def desp_num_temp(n):
    return render_template('5-number.html', number=n)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
