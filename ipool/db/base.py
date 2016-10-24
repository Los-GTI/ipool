#coding=utf-8
class Driver(object):

    def __init__(self, config):
        pass

    #Add to detail
    def add_detail(self, name, item):
        pass

    #Add to queue
    def add_queue(self,name):
        pass

    #Delete element by name
    def delete(self, name):
        pass

    #Pop the first element of the queue
    def get_queue(self):
        pass

    #Get the detail by name
    def get_detail(self, name):
        pass

    #Clear all element
    def clear(self):
        pass

    def count(self):
        return 0

    def exists(self, name):
        return False
