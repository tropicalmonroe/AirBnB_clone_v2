#!/usr/bin/python3
"""a Flask web application"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', defaults={'state_id': 'None'}, strict_slashes=False)
@app.route('/states/<path:state_id>', strict_slashes=False)
def states(state_id):
    """return render html/state route listing all states and cities"""
    states = storage.all('State').values()
    for state in states:
        if escape(state_id) == state.id:
            return render_template('9-states.html',
                                  states=state, name=state.name)
    return render_template('9-states.html', states=states, name=state_id)


@app.teardown_appcontext
def teardown(self):
    """alchemy session remove"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
