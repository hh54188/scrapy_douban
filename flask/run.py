from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time
from info import *

app = Flask(__name__)


LAST_FETCH_TIMESTAMP = time.time()
EXPIRE_TIME = 10 * 60
RESULT = [];

instance = Info()
RESULT = instance.fetch()


def isExpire():
    global LAST_FETCH_TIMESTAMP
    cur_time = time.time();
    time_span = cur_time - LAST_FETCH_TIMESTAMP;
    LAST_FETCH_TIMESTAMP = cur_time;
    if time_span > EXPIRE_TIME:
        return True
    else:
        return False

def search(keywords):
    result = [];
    for item in RESULT:
        title = item["title"]
        for word in keywords:
            if word in title:
                result.append(item)
                break

    return result

@app.route('/')
def welcome():
    isExpire()
    return render_template('index.html')


@app.route('/fetch')
def fetch():
    global RESULT
    keywords = request.args["param"].split("&")
    result = search(keywords);
    return json.dumps({
        'status': 'ok',
        'data': result
    })


@app.errorhandler(404)
def page_not_found(error):
    return "wrong"


app.config.update(
    DEBUG = True,
    SERVER_NAME = "127.0.0.1:8000"
)

if __name__ == '__main__':
    app.run()
