from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from wtforms import StringField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.orm import backref
from flask_socketio import SocketIO
import pandas as pd
import requests
from io import StringIO
import threading
import time
socketio = SocketIO()
from flask_socketio import SocketIO, emit


def fetch_latest_location():
    # Fetch the latest data from the CSV file
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT4UKPpECBy-SH7EQOHhWslM5knNZ8dGj39uU31K6ww_7OAl8N2U9vE3bWYeqVRf7TG9V204ivWbBsd/pub?output=csv"
    response = requests.get(csv_url)
    csv_data = response.text
    df = pd.read_csv(StringIO(csv_data))

    # Get the last row of the DataFrame
    last_row = df.iloc[-1]

    # Extract latitude and longitude data from the last row
    latitude = last_row['Latitude']
    longitude = last_row['Longitude']

    return {'latitude': latitude, 'longitude': longitude}