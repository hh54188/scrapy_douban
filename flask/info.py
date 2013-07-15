import urllib2
import time
import sys
from bs4 import BeautifulSoup

class Info(object):
    FETCH_URLS = [
        # "http://www.douban.com/group/beijingzufang/discussion",
        # "http://www.douban.com/group/fangzi/discussion",
        # "http://www.douban.com/group/262626/discussion",
        "http://www.douban.com/group/276176/discussion"
    ]

    RESULT = []
    PAUSE_SECOND = 2
    PAGE_NUM = 1

    def __init__(self):
        pass

    def __fetchSingle(self, url):
        # headers = { 
        #     'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #     'Cache-Control': 'no-cache',
        #     'Connection': 'keep-alive',
        #     'Host': 'www.douban.com'
        # }
        # request = urllib2.Request(url, None, headers)
        # page = urllib2.urlopen(request)
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
            self.RESULT.append(item)
            

    def fetch(self):
        for url in self.FETCH_URLS:
            for  i in range(self.PAGE_NUM):
                link = url + "?start=" + str(25 * i)
                time.sleep(self.PAUSE_SECOND)
                self.__fetchSingle(link)
        return self.RESULT
        # print sys.getsizeof(self.RESULT)