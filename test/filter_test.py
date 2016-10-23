#coding=utf-8
import pytest
import ipool.filter as filter

class TestFilter:
    def test_check(self):
        item = {
                'ip':'120.76.243.40',
                'port':'80',
                'protocol':'http'
                }
        print filter.IPChecker().check(item)
