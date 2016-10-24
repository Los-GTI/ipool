#!/usr/bin/python

from twisted.internet import reactor,defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from ipool.spiders.xici import XiciSpider
from ipool.spiders.ipbus import IpbusSpider
from ipool.spiders.mimiip import MimiipSpider

runner = CrawlerRunner(get_project_settings())
dfs = set()
dfs.add(runner.crawl(XiciSpider))
dfs.add(runner.crawl(MimiipSpider))
dfs.add(runner.crawl(IpbusSpider))

defer.DeferredList(dfs).addBoth(lambda _: reactor.stop())
reactor.run()
