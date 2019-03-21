# redis数据库地址
REDIS_HOST = "localhost"
# 端口
REDIS_PORT = 6379
# 密码 默认为NOne
REDIS_PASSWORD = None
#
REDIS_KEY = "proxies"

MAX_SCORE = 100

MIN_SCORE = 0

INITIAL_SCORE = 10

"""check模块"""
# 可用响应码
VALID_STATUS_CODES = [200]

TEXT_URL = "http://www.baidu.com"
# 最大协程数
BATCH_TEST_SIZE = 100

# 池中最大代理数目
POOL_MAX_THRESHOLD = 10000

'''scheduler模块'''
# 测试模块间隔
TESTER_CYCLE = 20

GETTER_CYCLE = 20
# 是否启动模块进程
TESTER_ENABLE = True

GETTER_ENABLE = True

API_ENABLE = True
# api主机端口
API_HOST = '0.0.0.0'
API_PORT = 5555
