#coding=utf-8
import redis

'''
使用redis作为ip池数据存储层
通过方向性（头出尾进）的方法来操作列表以实现队列来存储代理ip列表
使用hash来存储代理ip的详细信息
'''
class DB(object):

    def __init__(self):
        try:
            self.conn = redis.Redis(password = 'localtest')
        except:
            raise Exception('failed to connect redis')
        self.queue = 'ip_queue'

    #Add to detail
    def add_detail(self, name, item):
        self.conn.hmset(name, dict(item))

    #Add to queue
    def add_queue(self,name):
        self.conn.rpush(self.queue, name)

    #Delete element by name
    def delete(self, name):
        self.conn.delete(name)

    #Pop the first element of the queue
    def get_queue(self):
        return self.conn.lpop(self.queue)

    #Get the detail by name
    def get_detail(self, name):
        return self.conn.hgetall(name)

    #Clear all element
    def clear(self):
        name = self.conn.lpop(self.queue)
        while name:
            self.conn.delete(name)
            name = self.conn.lpop(self.queue)

    def count(self):
        return self.conn.llen(self.queue)

    def exists(self, name):
        return self.conn.exists(name)
