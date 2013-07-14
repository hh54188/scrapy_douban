import urllib2
import socket
import time
from bs4 import BeautifulSoup

class Info(object):
    FETCH_URLS = [
        "http://www.douban.com/group/beijingzufang/discussion"
    ]
    RESULT = []

    def __init__(self):
        pass

    def __fetchSingle(self, url):
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        collection = soup.select("table.olt td.title a")

        for link in collection:
            item = {
                "title": "",
                "link": ""
            }
            item["title"] = link["title"]
            item["link"] = link["href"]
            Info.RESULT.append(item)

            # title = link["title"]
            # href = link["href"]
            # print title
            

    def fetch(self):
        for url in Info.FETCH_URLS:
            for  i in range(10):
                link = url + "?start=" + str(25 * i)
                # print link
                time.sleep(3)
                self.__fetchSingle(link)
                print len(Info.RESULT)



instance = Info();
instance.fetch();