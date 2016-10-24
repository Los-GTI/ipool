#coding=utf-8
import ConfigParser
import os
import sys

class DB(object):
    current_path = os.path.dirname(__file__)
    config_file_path = os.path.abspath(os.path.join(current_path, os.pardir, os.pardir, 'config.ini'))

    def __init__(self):
        db_type, db_info = self.get_config()
        filename = 'db_' + db_type
        if os.path.isfile(os.path.join(self.current_path, filename + '.py')):
            sys.path.append(self.current_path)
            driver_module = __import__(filename)
        else:
            raise Exception('failed to import db driver')
        try:
            self.driver = driver_module.Driver(dict(db_info))
        except Exception,e:
            print e
            raise Exception('failed to connect db')

    def __getattr__(self, attr):
        def invoke_method(*args):
            return getattr(self.driver, attr)(*args)
        return invoke_method

    def get_config(self):
        cf = ConfigParser.ConfigParser()
        cf.read(self.config_file_path)
        db_type = cf.get('db', 'db_type')
        db_info = cf.items(db_type)
        return db_type,db_info
