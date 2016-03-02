from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from argparse import ArgumentParser
import json
import csv
import logging
import sys
import glob
from flask.ext.login import LoginManager
from flask_oauthlib.client import OAuth


app = Flask(__name__)
app.config.from_pyfile('../../config/config.py')
mail = Mail(app)

login_manager = LoginManager(app)
oauth = OAuth(app)

        # use Google as remote application
        # you must configure 3 values from Google APIs console
        # https://code.google.com/apis/console
google = oauth.remote_app('google', app_key='GOOGLE')
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.refresh_view = 'reauth'




