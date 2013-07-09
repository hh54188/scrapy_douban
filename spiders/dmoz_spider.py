from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class DmozSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/group/beijingzufang/discussion"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select("//table[@class='olt']/tr/td[@class='title']/a")
        print "!!!!!!!!!!"
        # print sites
        for row in rows:
            print row.select('text()').extract()[0]
            print row.select('@href').extract()[0]