"""
This script runs the MatchAPI_Dota2 application using a development server.
"""

from os import environ
from MatchAPI_Dota2 import app

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5555

if __name__ == "__main__":
    HOST = environ.get('SERVER_HOST', DEFAULT_HOST)
    try:
        PORT = int(environ.get('SERVER_PORT', DEFAULT_PORT))
    except ValueError:
        PORT = DEFAULT_PORT
    app.run(HOST, PORT)
