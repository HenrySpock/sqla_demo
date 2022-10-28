from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "thekey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
# This specifies that we are using postgres, and what database we are using. This has to be done first.



db = SQLAlchemy() 
# The above runs SQLAlchemy and stores it to the variable db, so most commands will looke like db.[]
db.app = app
db.init_app(app)
# db.app = app associates the app and the init command with he db variable 
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG_TB_INTERCEPT_REDIERECTS'] = False 
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')