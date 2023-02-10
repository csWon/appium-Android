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


import datetime
import logging
from Tickets import tickets
from DriverManager import driverManager
from LoggingManager import loggingManager

import traceback

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


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

    url_ip_check = 'https://ko.infobyip.com/'
    url_k_product = 'https://product.kyobobook.co.kr/'
    url_naver = 'https://www.naver.com'
    url_aladin = 'https://www.aladin.co.kr/'
    url_ypbook = 'https://www.ypbooks.co.kr/'



    _tickets = tickets()
    for ticket in _tickets.getTicket():
        # s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # logging.info('timeStamp : ' + s)
        for i in range(1, 500):
            start = time.time()
            dManager = driverManager()
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

            except Exception as e:
                print("exception!!! : ", traceback.format_exc())
                print("error occured")
                driver.quit()
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
                               deviceId=driverManager.dc.get("deviceName"), # TODO : multi 가능하게 한 뒤 device name 넣어주세여
                               status=status,
                               rank=rank,
                               loadTime=sec,
                               errorMsg=errorMsg);
                print('------------------------------')



    #
    #
    # print_hi('PyCharm')
    # options = webdriver.ChromeOptions()
    # options.add_argument()
    #
    # dc = {
    #     "platformName": "Android",
    #     "platformVersion": "9.0",
    #     "deviceName": "ce05171555816f1b03",
    #     "browserName": "chrome",
    #     "browserVersion": "109.0.5414.86"
    # }
    #
    # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)
    # driver.get("https://www.findip.kr/")
    # time.sleep(3)
    # driver.get("https://www.aladin.co.kr/")
    #
    # x_btn = driver.find_element(By.XPATH,'//*[@id="spaceEventLayer"]/div[1]/a[2]')
    # x_btn.click();
    # time.sleep(3)
    # bestbtn = driver.find_element(By.XPATH, '//*[@id="re_mallmenu"]/ul/li[3]/div/a/img')
    # bestbtn.click()
    # time.sleep(10)