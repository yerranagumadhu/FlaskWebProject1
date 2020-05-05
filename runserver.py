"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app
from flask_debugtoolbar import DebugToolbarExtension

# Need to use when we are dockerizing the Flask app
#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=int("5000"), debug=True)


#app.debug = True
#app.config['SECRET_KEY'] = 'DontTellAnyone'
#toolbar = DebugToolbarExtension(app)


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)