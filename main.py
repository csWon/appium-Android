# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from appium import webdriver
# from BookStore import bookStore
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string
import time

import Worker
import datetime
import logging
from Tickets import tickets
from DriverManager import driverManager
from LoggingManager import loggingManager

import traceback
from multiprocessing import Process, Queue

import unittest

import yaml

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def work(dc, server_ip):
    _tickets = tickets()
    for ticket in _tickets.getTicket():
        # s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # logging.info('timeStamp : ' + s)
        for i in range(1, 500):
            start = time.time()
            dManager = driverManager(dc, server_ip)
            logger = loggingManager()

            driver = dManager.open_browser_phone()

            status = 'S'
            errorMsg = ''
            try:
                keyword = ticket[1]
                page = ticket[2]
                n = ticket[3]
                title = ticket[4]

                print('cycle : ' + str(i))

                webPageClass = ticket[0](driver)

                # TODO : ranking return 해주세여
                rank = webPageClass.do(keyword, page, n, title)
                driver.quit()
                driver.__exit__()

            except Exception as e:
                print("exception!!! : ", traceback.format_exc())
                print("error occured")
                driver.quit()
                driver.__exit__()
                status = 'F'
                rank = 0
                errorMsg = traceback.format_exception_only(e)

            finally:
                sec = time.time() - start
                print (sec)
                times = str(datetime.timedelta(seconds=sec)).split(".")
                times = times[0]

                print("총 걸린시간 : " + times)

                logger.logging(site=ticket[0].__name__,
                               ticketNm=ticket[4],
                               deviceId=dManager.dc.get("deviceName"), # TODO : multi 가능하게 한 뒤 device name 넣어주세여
                               status=status,
                               rank=rank,
                               loadTime=sec,
                               errorMsg=errorMsg);
                driver.close()
                driver.stop_client()

                print('------------------------------')

# Press the green button in the gutter to run the script.


class AndroidSampleTest(unittest.TestCase):
    def __init__(self, method_name, dc, server_ip):
        super(AndroidSampleTest, self).__init__(method_name)
        self.desired_caps = dc
        self.server_ip = server_ip

    def setUp(self):
        # desired_caps = dc.copy()
        # desired_caps['deviceName'] = self.device_name
        # desired_caps['platformVersion'] = self.platform_ver
        dManager = driverManager(self.desired_caps, self.server_ip)
        self.driver = dManager.open_browser_phone()
        # self.driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(self.portNum), self.desired_caps)
        # self.driver.get('https://www.naver.com/')

    def tearDown(self):
        self.driver.quit()

    def test_for_android(self):
        self.driver.get('https://www.naver.com/')
        # assert el.text == 'Settings'

def tmp(suite):
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    # logger = logging.getLogger()
    # #
    # # # 로그의 출력 기준 설정
    # logger.setLevel(logging.INFO)
    # #
    # # # log 출력 형식
    # # # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # #
    # # # log 출력
    # stream_handler = logging.StreamHandler()
    # # # stream_handler.setFormatter(formatter)
    # logger.addHandler(stream_handler)
    #
    # s = datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss')
    # logfileName = 'log_' + s + '.log'
    # # logging.basicConfig(filename='./logs/'+logfileName, level=logging.INFO)
    # # logging.info('startTime : ' + s)
    #
    # # log를 파일에 출력
    # file_handler = logging.FileHandler('./logs/' + logfileName)
    # # # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    # deviceInfo.yml에서 디바이스 정보 파싱
    with open('deviceInfo.yml') as f:
        deviceInfo = yaml.load(f, Loader=yaml.FullLoader)

    deviceInfoLength = len(deviceInfo['device'].items())

    port = 4721
    suiteArr = []

    for k, v in deviceInfo['device'].items():
        suite = unittest.TestSuite()
        suite.addTest(Worker.worker('Do', v, '127.0.0.1:'+str(port)))
        suiteArr.append(suite)
        port += 1

    import multiprocessing

    with multiprocessing.Pool(processes=deviceInfoLength) as p:
        p.map(func=tmp, iterable=suiteArr)

