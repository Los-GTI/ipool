#!/usr/bin/python

from twisted.internet import reactor,defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from ipool.spiders.xici import XiciSpider
from ipool.spiders.ipbus import IpbusSpider
from ipool.spiders.mimiip import MimiipSpider
from ipool.spiders.kdl import KdlSpider
from ipool.spiders.goubanjia import GoubanjiaSpider

runner = CrawlerRunner(get_project_settings())
dfs = set()
dfs.add(runner.crawl(XiciSpider))
dfs.add(runner.crawl(MimiipSpider))
dfs.add(runner.crawl(IpbusSpider))
dfs.add(runner.crawl(KdlSpider))
dfs.add(runner.crawl(GoubanjiaSpider))

defer.DeferredList(dfs).addBoth(lambda _: reactor.stop())
reactor.run()
