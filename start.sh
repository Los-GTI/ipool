#!/bin/bash
cd `dirname $0`

scrapy crawl xici --logfile=log --loglevel=WARNING

scrapy crawl mimiip --logfile=log --loglevel=WARNING

scrapy crawl ipbus --logfile=log --loglevel=WARNING
