#coding=utf-8
import sys
import ipool.db as redis
import pytest
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        self.redis = redis.DB()
        self.name = '192.168.1.1:8080'
        self.value = {'ip':'192.168.1.1', 'port':'8080', 'potocol':'http'}
        self.redis.add_queue(self.name)
        self.redis.add_detail(self.name, self.value)

    def tearDown(self):
        self.redis.clear()

    def test_count(self):
        assert self.redis.count() == 1

    def test_add(self):
        name = '127.0.0.1:8080'
        value = {'ip':'127.0.0.1', 'port':'8080', 'potocol':'http'}
        self.redis.add_queue(name)
        self.redis.add_detail(name, value)
        assert self.redis.count() == 2

    def test_delete(self):
        name = self.redis.get_queue()
        if name:
            self.redis.delete(name)
        assert self.redis.count() == 0

    def test_get(self):
        assert self.name == self.redis.get_queue()
        assert self.value == self.redis.get_detail(self.name)
        self.redis.delete(self.name)

    def test_clear(self):
        name = '127.0.0.1:8080'
        value = {'ip':'127.0.0.1', 'port':'8080', 'potocol':'http'}
        self.redis.add_queue(name)
        self.redis.add_detail(name, value)
        self.redis.clear()
        assert self.redis.count() == 0
