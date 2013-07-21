import urllib2
import time
import sys
from bs4 import BeautifulSoup

class InfoClas(object):
    FETCH_URLS = [
        "http://www.douban.com/group/beijingzufang/discussion",
        "http://www.douban.com/group/fangzi/discussion",
        "http://www.douban.com/group/262626/discussion",
        "http://www.douban.com/group/276176/discussion"
    ]

    RESULT = []
    PAUSE_SECOND = 0
    PAGE_NUM = 1
    

    def __init__(self):
        pass


    def __showProgress(self, data):
        total = len(self.FETCH_URLS) * self.PAGE_NUM * 25
        print "[fecth progress]------>" + str((len(data) / float(total)) * 100) + '%'


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
            item["id"] = int(link["href"].split('/')[-2])
            self.RESULT.append(item)

            

    def fetch(self):
        self.RESULT = [];
        for url in self.FETCH_URLS:
            for  i in range(self.PAGE_NUM):
                link = url + "?start=" + str(25 * i)
                if (self.PAUSE_SECOND != 0):
                    time.sleep(self.PAUSE_SECOND)
                self.__fetchSingle(link)
                self.__showProgress(self.RESULT);
                # print sys.getsizeof(self.RESULT)
                # sorted
                result_sorted = sorted(self.RESULT, key=lambda x: x['id'], reverse = True)
        return result_sorted
        