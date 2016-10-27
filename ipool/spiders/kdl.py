# -*- coding: utf-8 -*-
import scrapy
from ipool.items import IpoolItem
import time

class KdlSpider(scrapy.Spider):
    name = "kdl"
    allowed_domains = ["kuaidaili.com"]
    start_urls = (
            'http://www.kuaidaili.com/free/inha/',
            'http://www.kuaidaili.com/free/intr/',
            'http://www.kuaidaili.com/free/outha/',
            'http://www.kuaidaili.com/free/outtr/',
    )

    def parse(self, response):
        for row in response.xpath('//table//tr'):
            tds = row.xpath('td');
            if len(tds) == 7:
                item = IpoolItem()
                item['ip'] = ''.join(tds[0].xpath('text()').extract())
                item['port'] = ''.join(tds[1].xpath('text()').extract())
                item['opacity'] = ''.join(tds[2].xpath('text()').extract())
                item['protocol'] = ''.join(tds[3].xpath('text()').extract()).lower()
                item['address'] = ''.join(tds[4].xpath('text()').extract())
                item['crawl_time'] = int(time.time())
                item['source'] = self.name
                yield item
