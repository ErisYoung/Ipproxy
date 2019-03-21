from multiprocessing import Process
import time
from api import app
from getter_proxy import Getter
from check_proxy import Tester
from settings import *

class Scheduler():
    def schedule_check(self,cycle=TESTER_CYCLE):
        check=Tester()
        while True:
            print("开始检测")
            check.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GETTER_CYCLE):
        getter=Getter()
        while True:
            print("开始抓取代理")
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        app.run()

    def run(self):
        print("代理池运行中")
        if GETTER_ENABLE:
            getter_process=Process(target=self.schedule_getter())
            getter_process.start()
        if TESTER_ENABLE:
            tester_process=Process(target=self.schedule_check())
            tester_process.start()
        if API_ENABLE:
            api_process=Process(target=self.schedule_api())
            api_process.start()


