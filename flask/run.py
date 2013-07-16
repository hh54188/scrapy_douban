# -*- coding: utf-8 -*- 
from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time
from info import *
from chart import *

app = Flask(__name__)

# the last fetch time
LAST_FETCH_TIMESTAMP = time.time()
# expire time
EXPIRE_TIME = 10 * 60
# fetch result
RESULT = []
# fetch result backup
RESULT_BACKUP = []
# the info crawl class
INFO_INSTANCE = InfoClas()
# is under fetch again
UNDER_FETCH = False


def update():
    global RESULT, INFO_INSTANCE, LAST_FETCH_TIMESTAMP, RESULT_BACKUP, UNDER_FETCH
    # resest
    RESULT = []
    print "[fetch data]------>begin"
    RESULT = INFO_INSTANCE.fetch()
    print "[fetch data]------>data length:" + str(len(RESULT))
    print "[fetch data]------>end"
    LAST_FETCH_TIMESTAMP = time.time()
    UNDER_FETCH = False

update()



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
    global RESULT, RESULT_BACKUP, UNDER_FETCH
    result = [];
    total = RESULT[:]    
    if UNDER_FETCH:
        total = UNDER_FETCH[:]
    for item in total:
        title = item["title"]
        for word in keywords:
            if word in title:
                result.append(item)
                total.remove(item)
                break
    return result


@app.route('/')
def welcome():
    global RESULT_BACKUP, UNDER_FETCH
    # if the data haven't update more than ten minutes
    # if isExpire():
    #     RESULT_BACKUP = RESULT
    #     UNDER_FETCH = True
    #     update()
    return render_template('index.html')
    


@app.route('/analysis')
def analysis():
    global RESULT
    instance = ChartClas()
    result = instance.analysis(RESULT)
    return json.dumps(result)
    


@app.route('/fetch')
def fetch():
    global RESULT, LAST_FETCH_TIMESTAMP, RESULT_BACKUP
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
