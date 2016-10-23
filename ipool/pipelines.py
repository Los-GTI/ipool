# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import db
import filter

class IpoolPipeline(object):
    def __init__(self):
        self.db = db.DB()
        self.filter = filter.IPChecker()

    def process_item(self, item, spider):
        name = '%s:%s' % (item['ip'], item['port'])

        if item['protocol'] not in ('http', 'https'):
            raise DropItem('Protocol not suitable: %s' % item['protocol'])

        if self.db.exists(name):
            raise DropItem('Duplicate item: %s' % item)

        verified = self.filter.check(item)
        if not verified:
            raise DropItem('Not available: %s' % item)

        self.db.add_queue(name)
        self.db.add_detail(name, verified)
        return verified

    def __del__(self):
        pass
