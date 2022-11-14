#!/usr/bin/python3
"""flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """html template /states_list route all states"""
    return render_template('7-states_list.html', states=storage.all('State').values())

@app.teardown_appcontext
def teardown(self):
    """remove sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
