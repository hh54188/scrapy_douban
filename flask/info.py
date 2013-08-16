# -*- coding: utf-8 -*- 

import urllib2
import time
import sys
from bs4 import BeautifulSoup

class InfoClas(object):
    FETCH_URLS = [
        "http://www.douban.com/group/beijingzufang/discussion",
        "http://www.douban.com/group/fangzi/discussion",
        "http://www.douban.com/group/262626/discussion",
        "http://www.douban.com/group/276176/discussion",

        # 北京租房豆瓣
        "http://www.douban.com/group/26926/discussion",
        # 北京租房（密探）
        "http://www.douban.com/group/sweethome/discussion",
        # 北京租房！找伴儿一起住一个房间！
        "http://www.douban.com/group/242806/discussion",
        # 北京租房房东联盟(中介勿扰) 
        "http://www.douban.com/group/257523/discussion",
        # 北京租房（非中介） 
        "http://www.douban.com/group/279962/discussion",
        # 北京租房合租房
        "http://www.douban.com/group/334449/discussion"
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
        try:
            page = urllib2.urlopen(url)
        except:
            return

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
        