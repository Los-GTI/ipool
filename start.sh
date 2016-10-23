#!/bin/bash
cd `dirname $0`

scrapy crawl xici --logfile=log --loglevel=INFO

scrapy crawl mimiip --logfile=log --loglevel=INFO

scrapy crawl ipbus --logfile=log --loglevel=INFO
