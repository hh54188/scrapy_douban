from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from spiders.dmoz_spider import DmozSpider
from scrapy.xlib.pydispatch import dispatcher

def stop_reactor():
    reactor.stop()

dispatcher.connect(stop_reactor, signal=signals.spider_closed)
spider = DmozSpider()
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start(loglevel=log.DEBUG)
log.msg("------------>Running reactor")
reactor.run()
log.msg("------------>Running stoped")
