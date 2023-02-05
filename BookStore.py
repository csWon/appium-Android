import time
import logging
import random
import datetime

class bookStore:
    url_ip_check = 'https://ko.infobyip.com/'
    url_k_product = 'https://product.kyobobook.co.kr/'
    url_naver = 'https://www.naver.com'
    url_aladin = 'https://www.aladin.co.kr/'
    url_ypbook = 'https://www.ypbooks.co.kr/'
    # def __init__(self):
    #     test = 1

    def getTargetElement(self, elements, title):
        idx = 0
        for e in elements:
            idx = idx + 1
            t = e.text.find(title)
            if e.text.find(title) != -1:
                logging.info('book idx : ' + str(idx))
                return e
            # if e.text==title:
            #     return e
        # document.getElementsByClassName('prod_info')[0].children[2].textContent

        logging.info("해당 페이지에서 물건 찾지 못함")
        return 'empty'

    def printFuncInfo(self, siteName, keyword, page, n):
        logging.info(siteName)
        logging.info("keyword : " + keyword + " / input page:" + str(page) + " / n:")

    def delay_n(self, n):
        wait_time = random.uniform(n, n+2)
        time.sleep(wait_time)

    def delay(self):
        self.delay_n(1)
        # wait_time = random.uniform(15, 20)
        # driver.implicitly_wait(wait_time)

    def delay_10(self):
        self.delay_n(10)
        # wait_time = random.uniform(15, 20)
        # driver.implicitly_wait(wait_time)