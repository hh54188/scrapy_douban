# -*- coding: utf-8 -*- 
from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time
from info import *
from chart import *

app = Flask(__name__)


LAST_FETCH_TIMESTAMP = time.time()
EXPIRE_TIME = 10 * 60
RESULT = [];

print "[fetch data]------>begin"
instance = InfoClas()
RESULT = instance.fetch()
print "[fetch data]------>data length:" + str(len(RESULT))
print "[fetch data]------>end"

# statistics
def chart():
    pass

def isExpire():
    global LAST_FETCH_TIMESTAMP
    cur_time = time.time();
    time_span = cur_time - LAST_FETCH_TIMESTAMP;
    print "[time span]------>span:" + str(time_span)
    if time_span > EXPIRE_TIME:
        return True
    else:
        return False

def search(keywords):
    global RESULT
    result = [];
    total = RESULT[:]
    for item in total:
        title = item["title"]
        for word in keywords:
            if word in title:
                result.append(item)
                total.remove(item)
                break
    return result

def reFetch():
    global RESULT
    RESULT = instance.fetch()


@app.route('/')
def welcome():
    # if the data haven't update more than ten minutes
    # if isExpire():
    #     reFetch()
    #     LAST_FETCH_TIMESTAMP = time.time()
    return render_template('index.html')


@app.route('/refresh')
def refresh():
    reFetch()


@app.route('/analysis')
def analysis():
    global RESULT
    instance = ChartClas()
    result = instance.analysis(RESULT)
    return json.dumps(result)
    


@app.route('/fetch')
def fetch():
    global RESULT
    global LAST_FETCH_TIMESTAMP
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
    app.run(use_reloader = False)
