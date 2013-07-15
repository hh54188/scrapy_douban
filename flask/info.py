import urllib2
import time
import sys
from bs4 import BeautifulSoup

class InfoClas(object):
    FETCH_URLS = [
        # "http://www.douban.com/group/beijingzufang/discussion",
        # "http://www.douban.com/group/fangzi/discussion",
        # "http://www.douban.com/group/262626/discussion",
        "http://www.douban.com/group/276176/discussion"
    ]

    RESULT = []
    PAUSE_SECOND = 1
    PAGE_NUM = 1

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
            print "[under fetch]------>:" + link["href"]
            item["link"] = link["href"]
            self.RESULT.append(item)
            

    def fetch(self):
        for url in self.FETCH_URLS:
            for  i in range(self.PAGE_NUM):
                link = url + "?start=" + str(25 * i)
                if (self.PAUSE_SECOND != 0):
                    time.sleep(self.PAUSE_SECOND)
                self.__fetchSingle(link)
        return self.RESULT
        # print sys.getsizeof(self.RESULT)