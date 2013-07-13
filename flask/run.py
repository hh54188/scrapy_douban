from flask import Flask, url_for
from flask import request
from flask import render_template
# bs4
import urllib2
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    page = urllib2.urlopen("http://www.douban.com/group/beijingzufang/discussion")
    soup = BeautifulSoup(page)
    collection = soup.select("table.olt td.title a")

    for link in collection:
        title = link["title"]
        href = link["href"]

        print title
        print href
    # return 'Hello World!'
    # for i in range(10000):
    #   print i
    return render_template('index.html')

@app.route('/login/<username>')
def login(username):
    return 'login %s' % (username)

# @app.route('/login/<username>', methods="POST")
# def login():
#   return 'login'

@app.errorhandler(404)
def page_not_found(error):
    return "wrong"

app.config.update(
    DEBUG = True,
    SERVER_NAME = "127.0.0.1:8000"
)
if __name__ == '__main__':
    app.run()
