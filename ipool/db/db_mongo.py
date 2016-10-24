#coding=utf-8
import pymongo
import ipool.db.base as base

'''
使用mongodb作为ip池数据存储层
'''
class Driver(base.Driver):
    pk = 'socket'
    def __init__(self, config):
        super(Driver, self).__init__(config)
        try:
            self.client = pymongo.MongoClient(host=config['host'], port=int(config['port']))
            self.db = self.client[config['db']]
            self.collection = self.db[config['collection']]
        except Exception, e:
            print e
            raise Exception('failed to connect mongo')

    #Add to detail
    def add_detail(self, name, item):
        item = dict(item)
        item[self.pk] = name
        self.collection.insert(item)

    #Add to queue
    def add_queue(self,name):
        pass

    #Delete element by name
    def delete(self, name):
        self.collection.delete_one({self.pk: name})

    #Pop the first element of the queue
    def get_queue(self):
        document = list(self.collection.find({self.pk: {'$ne': None}}).sort('verify_time', 1).limit(1))
        if document:
            document = document[0]
            return document[self.pk]

    #Get the detail by name
    def get_detail(self, name):
        document = self.collection.find_one({self.pk: name})
        if document:
            del document['_id']
            return document

    #Clear all element
    def clear(self):
        self.collection.delete_many({})

    def count(self):
        return self.collection.count({})

    def exists(self, name):
        return self.collection.count({self.pk: name}) > 0
