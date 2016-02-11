"""
The flask application package.
"""

from flask import Flask
import MatchAPI_Dota2.matches

app = Flask(__name__)

match_controller = matches.Matches()
match_controller.start()

# This import requires app to be defined
import MatchAPI_Dota2.views


