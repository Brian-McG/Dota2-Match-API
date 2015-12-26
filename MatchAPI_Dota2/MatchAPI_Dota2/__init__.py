"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

from MatchAPI_Dota2 import matches
match_controller = matches.Matches()
match_controller.start()

import MatchAPI_Dota2.views
