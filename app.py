from flask import Flask, Response, render_template, jsonify, request
from flask_basicauth import BasicAuth
from icalendar import Calendar, Event
from flask import send_from_directory

import schedule
import time
from feed import fetch_crawlers

import json
import os
import requests

def read_json(path):
    with open(path) as f:
        return json.load(f)
    
# Get the absolute path to the static directory
STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='/')

secrets = read_json("secrets/secrets.json")
settings = read_json("application.json")

app.config['BASIC_AUTH_USERNAME'] = secrets['username']
app.config['BASIC_AUTH_PASSWORD'] = secrets['password']

basic_auth = BasicAuth(app)

last_refresh = None



'''
-----------------------------------------------------

Section for App-specific functions

-----------------------------------------------------
'''

def fetch_and_store_calendars():
    """
    Fetch ICS files from URLs in static/calendars.json and save as static/<name>.ics
    """
    calendars_path = os.path.join('static', 'calendars.json')
    if not os.path.exists(calendars_path):
        print(f"{calendars_path} not found.")
        return
    with open(calendars_path) as f:
        calendars = json.load(f)
    for cal in calendars:
        name = cal.get('name')
        url = cal.get('calendar_url')
        if not name or not url:
            continue
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                ics_path = os.path.join('static', f'{name}.ics')
                with open(ics_path, 'w', encoding='utf-8') as ics_file:
                    ics_file.write(resp.text)
                print(f"Fetched and saved {name}.ics")
            else:
                print(f"Failed to fetch {url}: {resp.status_code}")
        except Exception as e:
            print(f"Error fetching {url}: {e}")

def fetch_crawlers_if_required():
    global last_refresh
    if last_refresh is None or time.time() - last_refresh > settings['refresh_interval']:
        fetch_crawlers()
        fetch_and_store_calendars()
        last_refresh = time.time()

@app.route('/news')
@app.route('/presentation')
@app.route('/')
def presentation():
    fetch_crawlers_if_required()
    feed = read_json("feed.json")

    return render_template('reveal.html', feed=feed)


'''
-----------------------------------------------------

Section for template functions

-----------------------------------------------------
'''

@app.route('/about')
def about():
    return render_template('about.html', **read_json("application.json"))

@app.route('/secret')
@basic_auth.required
def secret_page():
    return "You have access to the secret page!"


@app.route('/logs')
@basic_auth.required
def logs():
    log_messages = []
    with open('application.log', 'r') as logfile:
        for line in logfile:
            try:
                time, application, log_type, message = line.strip().split(' ', 3)
                log_messages.append({'time': time, 'application': application, 'type': log_type, 'message': message})
            except Exception as e:
                print("Parse Error for log event:" + line)
    log_messages = log_messages[::-1]  # Reverse the order of the messages to display the latest message first
    return render_template('logs.html', log_messages=log_messages)


if __name__ == '__main__':
    app.run()