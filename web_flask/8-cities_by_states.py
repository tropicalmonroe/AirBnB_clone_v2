
#!/usr/bin/python3
"""a Flask web application"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """tml template at the /8-cities_by_states route,list all cities"""
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """sql alchemy session removed"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
