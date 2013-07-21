# -*- coding: utf-8 -*- 
from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time
from info import *
from chart import *
from mongo import *

app = Flask(__name__)

# the last fetch time
LAST_FETCH_TIMESTAMP = time.time()
# expire time
EXPIRE_TIME = 15 * 60
# fetch result
RESULT = []
# the info crawl class
INFO_INSTANCE = InfoClas()
# mongo operation
DB_INSTANCE = MongoDBClas()


def update():
    global RESULT, INFO_INSTANCE, LAST_FETCH_TIMESTAMP, DB_INSTANCE
    # resest
    RESULT = []
    print "[fetch data]------>begin"
    RESULT = INFO_INSTANCE.fetch()
    print "[fetch data]------>data length:" + str(len(RESULT))
    print "[fetch data]------>end"
    LAST_FETCH_TIMESTAMP = time.time()
    # 数据获取完毕

    # 从数据库中读取
    RESULT_DB = DB_INSTANCE.findAll()
    print "[DB operation]------>DB data length:" + str(len(RESULT_DB))

    # 与新数据对比并且筛选
    for new_item in RESULT:
        flag = False
        for old_item in RESULT_DB:
            if new_item["id"] == old_item["id"]:
                flag = True
                break
        if flag == False:
            RESULT_DB.append(new_item)
    RESULT = sorted(RESULT_DB, key=lambda x: x['id'], reverse = True)
    print "[DB operation]------>merge data length:" + str(len(RESULT_DB))
    if len(RESULT) > 1000:
        RESULT = RESULT[:1000]

    # 清空并且重写
    DB_INSTANCE.clear()
    DB_INSTANCE.save(RESULT)


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
    global RESULT, DB_INSTANCE
    result = [];
    total = DB_INSTANCE.findAll()
    for item in total:
        title = item["title"]
        for word in keywords:
            if word in title:
                result.append(item)
                total.remove(item)
                break
    result = sorted(result, key=lambda x: x['id'], reverse = True)                
    return result


@app.route('/refresh')
def refresh():
    # if the data haven't update more than ten minutes
    # 因为部署在平台上，只能使用单线程更新，只有更新完才能相应用户
    if isExpire():
        update()
    return json.dumps({
        'status': 'ok'
    })

@app.route('/force')
def force_refresh():
    global RESULT
    update()
    return json.dumps({
        'status': 'ok',
        'data': len(RESULT)
    })  

@app.route('/')
def welcome():
    global RESULT
    return render_template('index.html', data_length = len(RESULT))
    


@app.route('/analysis')
def analysis():
    global RESULT
    instance = ChartClas()
    result = instance.analysis(RESULT)
    return json.dumps(result)
    


@app.route('/fetch')
def fetch():
    global RESULT, LAST_FETCH_TIMESTAMP
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
