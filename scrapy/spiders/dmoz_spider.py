from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from items import DmozItem
import threading

class DmozSpider(BaseSpider):
    name = "douban" 
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/group/beijingzufang/discussion"
    ]

    def __init__(self):
        pass


    def set_interval(func, sec):
        def func_wrapper():
            set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t    

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select("//table[@class='olt']/tr/td[@class='title']/a")
        items = []
        # print sites
        for row in rows:
            print row.select('text()').extract()[0]
            print row.select('@href').extract()[0]

            item = DmozItem()
            item["title"] = row.select('text()').extract()[0]
            item["link"] = row.select('@href').extract()[0]
            items.append(item)


        print "-------------------->find the length"
        print len(items)
        return items