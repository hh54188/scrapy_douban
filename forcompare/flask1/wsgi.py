# -*- coding: utf-8 -*- 
from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time

application = app = Flask(__name__)

# the last fetch time
LAST_FETCH_TIMESTAMP = time.time()
# expire time
EXPIRE_TIME = 15 * 60
# fetch result
RESULT = []
# fetch result backup
RESULT_BACKUP = []
# the info crawl class
INFO_INSTANCE = InfoClas()
# is under fetch again
UNDER_FETCH = False

@app.route('/fetch')
def fetch():
    # global RESULT, LAST_FETCH_TIMESTAMP, RESULT_BACKUP
    # keywords = request.args["param"].split("&")
    # result = search(keywords);
    return json.dumps({
        'status': 'ok'
        # 'data': result
    })


@app.route('/')
def welcome():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return "wrong"



app.config.update(
    DEBUG = True
)

if __name__ == '__main__':
    app.run(use_reloader = False)