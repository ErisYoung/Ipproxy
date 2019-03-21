import time
import asyncio
import aiohttp
from aiohttp.client_exceptions import ClientError,ClientConnectionError
from save import RedisClient
from settings import *


class Tester():
    def __init__(self):
        self.redis=RedisClient()

    async def test_single_proxy(self,proxy):
        conn=aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy=proxy.decode("utf-8")
                http_proxy="http://"+proxy
                print("测试代理{}中".format(proxy))
                async with session.get(TEXT_URL,proxy=http_proxy,timeout=15) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print("代理可用",proxy)
                    else:
                        self.redis.decrease(proxy)
                        print("代理返回的响应码不合法",proxy)

            except (ClientConnectionError,ClientError,AttributeError,asyncio.TimeoutError):
                self.redis.decrease(proxy)


    def run(self):
        print("测试开始运行")
        try:
            proxies=self.redis.all()
            loop=asyncio.get_event_loop()
            for i in range(0,len(proxies),BATCH_TEST_SIZE):
                test_proxies=proxies[i:i+BATCH_TEST_SIZE]
                tasks=[self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print("测试发生错误",e.args)
