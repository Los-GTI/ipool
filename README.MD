#IPool
代理ip池，基于Scrapy开发的第一个Scrapy练手项目

采集http代理和https代理

数据存储层支持Redis和Mongodb。

###使用方法：
下载源码
```
git clone https://github.com/SatanSec/ipool
```
编辑项目目录下的config.ini，配置自己的数据库

db_type处为redis和mongo二选一，根据自己的情况修改相应的配置
```
[db]
db_type = mongo

[redis]
host = 127.0.0.1
port = 6379
db = 0
password = passwd

[mongo]
host = 127.0.0.1
port = 27017
db = ipool
collection = detail
```
启动：
* 从命令行运行scrapy crawl spidername（运行单个爬虫）
* 运行start.py
* 运行start.sh
start.py和start.sh可运行所有爬虫。推荐使用start.py，如果start.py无法正常采集则使用start.sh

###数据来源：
* [西刺代理](http://www.xicidaili.com/)
* [ip巴士](http://ip84.com/gn)
* [秘密ip](http://www.mimiip.com/gngao/)
* [快代理](http://www.kuaidaili.com/free/inha/)
* [http://www.goubanjia.com](http://www.goubanjia.com/free/gngn/index.shtml)

后期将开放数据