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

print "[fetch data]------>begin"
instance = Info()
RESULT = instance.fetch()
print "[fetch data]------>data length:" + str(len(RESULT))
print "[fetch data]------>end"

def isExpire():
    global LAST_FETCH_TIMESTAMP
    cur_time = time.time();
    time_span = cur_time - LAST_FETCH_TIMESTAMP;
    print "------>Time span:" + str(time_span)
    if time_span > EXPIRE_TIME:
        return True
    else:
        return False

def search(keywords):
    global RESULT
    result = [];
    total = RESULT[:]
    print "[search data]------>RESULT len:" + str(len(RESULT))
    print "[search data]------>total len:" + str(len(total))
    print "[search data]------>keywords len:" + str(len(keywords))
    for item in total:
        title = item["title"]
        for word in keywords:
            if word in title:
                result.append(item)
                total.remove(item)
                break
    print "[search data]------>result len:" + str(len(result))
    return result

def reFetch():
    global RESULT
    RESULT = instance.fetch()


@app.route('/')
def welcome():
    isExpire()
    return render_template('index.html')


@app.route('/refresh')
def refresh():
    reFetch()


@app.route('/fetch')
def fetch():
    global RESULT
    keywords = request.args["param"].split("&")
    result = search(keywords);
    # if the data haven't update more than ten minutes
    if isExpire():
        reFetch()
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
