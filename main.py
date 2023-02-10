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

import traceback
from multiprocessing import Process, Queue

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

            driver = dManager.open_browser_phone()

            try:
                keyword = ticket[1]
                page = ticket[2]
                n = ticket[3]
                title = ticket[4]

                print('cycle : ' + str(i))

                webPageClass = ticket[0](driver)
                webPageClass.do(keyword, page, n, title)

                # driver.quit()

            except Exception as e:
                # print("exception!!! : ", traceback.format_exc())
                print("error occured")
                driver.quit()
            finally:
                sec = time.time() - start
                times = str(datetime.timedelta(seconds=sec)).split(".")
                times = times[0]

                print("총 걸린시간 : " + times)
                print('------------------------------')

# Press the green button in the gutter to run the script.
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


    dc = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce0317136d6b60b10c",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.117"
    }

    dc2 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce05171555816f1b03",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.86"
    }

    th1 = Process(target=work, args=(dc,"127.0.0.1:4723"))
    # th2 = Process(target=work, args=(dc2,))

    th1.start()
    # th2.start()
    th1.join()
    # th2.join()


