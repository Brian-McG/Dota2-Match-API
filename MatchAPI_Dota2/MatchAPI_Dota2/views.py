"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MatchAPI_Dota2 import app
from MatchAPI_Dota2 import match_controller

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/match_api')
def match_api():
    """Json of current and upcoming games"""
    return render_template(
        'matches.json',
        json_block=match_controller.list_of_matches
    )
