import urllib2
import time
import sys
from bs4 import BeautifulSoup

class Info(object):
    FETCH_URLS = [
        "http://www.douban.com/group/beijingzufang/discussion",
        "http://www.douban.com/group/fangzi/discussion",
        "http://www.douban.com/group/262626/discussion",
        "http://www.douban.com/group/276176/discussion"
    ]

    RESULT = []
    PAUSE_SECOND = 2
    PAGE_NUM = 10

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
            

    def fetch(self):
        for url in Info.FETCH_URLS:
            for  i in range(Info.PAGE_NUM):
                link = url + "?start=" + str(25 * i)
                time.sleep(Info.PAUSE_SECOND)
                self.__fetchSingle(link)
                print len(Info.RESULT)
        print sys.getsizeof(Info.RESULT)



instance = Info();
instance.fetch();