from flask import Flask, Response, render_template, jsonify, request
from flask_basicauth import BasicAuth
from icalendar import Calendar, Event

import schedule
import time
from feed import fetch_crawlers

import json

def read_json(path):
    with open(path) as f:
        return json.load(f)

app = Flask(__name__)

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

def fetch_crawlers_if_required():
    global last_refresh
    if last_refresh is None or time.time() - last_refresh > settings['refresh_interval']:
        fetch_crawlers()
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