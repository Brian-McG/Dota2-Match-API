"""
The flask application package.
"""

import logging
from flask import Flask
import MatchAPI_Dota2.matches

logging.basicConfig(filename="Dota2-Match-API.log", level=logging.INFO)

app = Flask(__name__)

match_controller = matches.Matches()
match_controller.start()

# This import requires app to be defined
import MatchAPI_Dota2.views


