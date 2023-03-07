from flask import Flask, Response, render_template, jsonify, request
from flask_basicauth import BasicAuth
from icalendar import Calendar, Event

import schedule
import time
import subprocess

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

program_status = "not running"

'''
-----------------------------------------------------

Section for App-specific functions

-----------------------------------------------------
'''

@app.route('/news')
def news():
    feed_elements = read_json("app/feed.json")

    try:
        item_number = int(request.args.get('item'))
        article = feed_elements[item_number]
    except:
        article = feed_elements[0]

    return render_template('feed_slide.html', article=article)


'''
-----------------------------------------------------

Section for template functions

-----------------------------------------------------
'''

@app.route('/')
def index():
    return render_template('index.html', **read_json("application.json"))

@app.route('/secret')
@basic_auth.required
def secret_page():
    return "You have access to the secret page!"

@app.route('/status')
def status():
    global program_status
    return jsonify(status=program_status)

@app.route('/logs')
@basic_auth.required
def logs():
    log_messages = []
    with open('app/log/application.log', 'r') as logfile:
        for line in logfile:
            try:
                time, application, log_type, message = line.strip().split(' ', 3)
                log_messages.append({'time': time, 'application': application, 'type': log_type, 'message': message})
            except Exception as e:
                print("Parse Error for log event:" + line)
    log_messages = log_messages[::-1]  # Reverse the order of the messages to display the latest message first
    return render_template('logs.html', log_messages=log_messages)


@app.route('/activate', methods=['POST'])
def activate():
    global program_status
    if program_status == "success":
        return jsonify(status='already running')
    program_running = True
    if start():
        program_status = "success"
    else:
        program_status = "failed"
    return jsonify(status=program_status)

def start():
    time.sleep(5)
    # code for your function goes here
    subprocess.Popen(["python", "app/main.py"]) 
    print("Crawler started.")
    return True

if __name__ == '__main__':
    app.run()