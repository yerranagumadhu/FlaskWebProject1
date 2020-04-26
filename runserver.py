"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
