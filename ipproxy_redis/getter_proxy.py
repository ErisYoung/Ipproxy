from save import RedisClient
from crawler import Crawler
from settings import *


class Getter():
    def __init__(self):
        self.redis=RedisClient()
        self.crawler=Crawler()

    def is_over_threshold(self):
        if self.redis.count()>=POOL_MAX_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print("获取器开始执行")
        if not self.is_over_threshold():
            for callback_index in range(self.crawler.__CrawlFuncCount__):
                # print(callback_index)
                callback=self.crawler.__CrawlFunc__[callback_index]
                proxies =self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)

