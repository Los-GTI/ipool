#!/usr/bin/python
#coding=utf-8
from ipool.filter import IPChecker
from ipool.db import DB

data = DB()
verifier = IPChecker()
length = data.count()
count = 0
first = name = ''
while count < length:
    name = data.get_queue()
    #完成一轮校验
    if first and name == first:
        break
    detail = data.get_detail(name)
    detail = verifier.check(detail)
    if detail:
        data.add_queue(name)
        if not first:
            first = name
    else:
        data.delete(name)
    count += 1
