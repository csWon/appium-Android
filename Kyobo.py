from BookStore import bookStore
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random

class kyobo(bookStore):
    def __init__(self, driver):
        # bookStore.__init__(self)
        self.driver = driver

    def do(self, keyword, page, n, title):
        self.kyobo_best_v1(keyword, page, n, title)

    def kyobo_v1(self, keyword, page, n, title):
        super().printFuncInfo(self.kyobo.__name__, keyword, page, n)
        page = page - 1
        n = n - 1
        super().driver.get(super().url_k_product)
        logging.info('start kyobo')
        print('start kyobo_v1')
        # // 돋보기 눌려서 product.kyobobook.co.kr로 진입
        # btn = driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
        # btn.click()
        #
        # # btn_header_search
        # btn = driver.find_element(By.CLASS_NAME, 'btn_header_search')
        # btn.click()
        #
        # # // 검색하기 전 단계로 진입하기
        # search_box = driver.find_element(By.CLASS_NAME, 'btn_header_search')

        # search_box = driver.find_element(By.CLASS_NAME, 'ip_gnb_search')
        # search_box.send_keys('사국지')
        super().delay()
        # 검색창 클릭
        search_box = self.driver.find_element(By.ID, 'searchKeyword')
        search_box.click()
        super().delay()
        search_box.send_keys(keyword)
        super().delay()

        btn = self.driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
        btn.click()
        super().delay()

        # 페이지 이동
        # document.getElementsByClassName('btn_page_num')[5]

        btn = self.driver.find_elements(By.CLASS_NAME, 'btn_page_num')
        btn[page].click()
        super().delay()

        # 물건 클릭
        elements = self.driver.find_elements(By.CLASS_NAME, 'prod_info')
        target = super().getTargetElement(elements, title)
        if target == 'empty':
            return;
        target.click()

        self.driver.implicitly_wait(20)
        # targetProduct = driver.find_element(By.CLASS_NAME, 'prod_info')
        # targetProduct = driver.find_elements(By.CLASS_NAME, 'prod_link')
        # targetProduct[n].click()
        # driver.find_element_by_xpath('//*[@class="prod_link"]').send_keys(Keys.ENTER)
        # targetProduct.click()
        # targetProduct.send_keys(Keys.ENTER)
        logging.info(self.driver.title)
        logging.info(self.driver.current_url)
        super().delay_n(60)

    def kyobo_v2(self, keyword, page, n, title):
        super().printFuncInfo(self.kyobo_v2.__name__, keyword, page, n)
        page = page - 1
        n = n - 1
        self.driver.get(super().url_k_product)
        print('start kyobo_v2')
        # // 돋보기 눌려서 product.kyobobook.co.kr로 진입
        # btn = driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
        # btn.click()
        #
        # # btn_header_search
        # btn = driver.find_element(By.CLASS_NAME, 'btn_header_search')
        # btn.click()
        #
        # # // 검색하기 전 단계로 진입하기
        # search_box = driver.find_element(By.CLASS_NAME, 'btn_header_search')

        # search_box = driver.find_element(By.CLASS_NAME, 'ip_gnb_search')
        # search_box.send_keys('사국지')
        super().delay()
        # 검색창 클릭
        search_box = self.driver.find_element(By.ID, 'searchKeyword')
        search_box.click()
        super().delay()
        search_box.send_keys(keyword)
        super().delay()

        btn = self.driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
        btn.click()
        super().delay()

        for i in range(1, 5):
            tryPage = page - 1 + i
            logging.info("tryPage " + str(tryPage + 1))
            btn = self.driver.find_elements(By.CLASS_NAME, 'btn_page_num')
            btn[tryPage].click()
            super().delay()

            # 물건 클릭
            elements = self.driver.find_elements(By.CLASS_NAME, 'prod_info')
            target = super().getTargetElement(elements, title)
            if target == 'empty':
                continue
            else:
                logging.info("clickPage" + str(tryPage + 1))
                target.click()
                break

        self.driver.implicitly_wait(20)
        # targetProduct = driver.find_element(By.CLASS_NAME, 'prod_info')
        # targetProduct = driver.find_elements(By.CLASS_NAME, 'prod_link')
        # targetProduct[n].click()
        # driver.find_element_by_xpath('//*[@class="prod_link"]').send_keys(Keys.ENTER)
        # targetProduct.click()
        # targetProduct.send_keys(Keys.ENTER)
        logging.info(self.driver.title)
        logging.info(self.driver.current_url)
        super().delay_n(60)

    def kyobo_best_v1(self, keyword, page, n, title):
        super().printFuncInfo(self.kyobo_best_v1.__name__, keyword, page, n)
        page = page - 1
        n = n - 1
        self.driver.get(self.url_k_product)
        self.driver.implicitly_wait(10)
        super().delay()


        logging.info('start kyobo')
        # // 돋보기 눌려서 product.kyobobook.co.kr로 진입
        btn = self.driver.find_element(By.XPATH, '//*[@id="mainDiv"]/header/div[3]/a[1]')
        btn.send_keys(Keys.ENTER)

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=2)

        super().delay()
        for fkeyword in Keyword_3:
             # 검색창 클릭
             print(fkeyword + " searching")
             self.driver.implicitly_wait(10)
             super().delay_n(3)
             search_box = self.driver.find_element(By.ID, 'searchKeyword')
             search_box.click()

             self.driver.implicitly_wait(10)
             super().delay_n(2)
             search_box.send_keys(fkeyword)
             search_box.send_keys(Keys.ENTER)
             #
             # self.driver.implicitly_wait(10)
             # super().delay_n(2)
             # btn = self.driver.find_element(By.XPATH, '//*[@id="searchDiv"]/header/div[2]/div/a')
             # btn.send_keys(Keys.ENTER)

             ActionChains(self.driver).scroll_by_amount(0, 223).perform();

             self.driver.implicitly_wait(10)
             super().delay_n(2)
             btn = self.driver.find_element(By.XPATH, '//*[@id="mainDiv"]/header/div[2]/div/div/button')
             btn.click()

        super().delay_n(3)
        self.driver.implicitly_wait(10)
        self.driver.get(super().url_k_product)

        self.driver.implicitly_wait(10)
        ActionChains(self.driver).scroll_by_amount(0, 243).perform();

        best = self.driver.find_element(By.XPATH, '//*[@id="contents"]/div[4]/div[2]/div[1]/div/a/span[1]')
        best.click()
        super().delay_n(2)
        self.driver.implicitly_wait(20)
        print("베스트 이동")

        i = 0
        isClicked = False

        for page in range(50):
            prods = self.driver.find_elements(By.CLASS_NAME, "prod_info")
            ActionChains(self.driver).move_to_element(prods[-2]).perform()
            j = 0

            for prod in prods[i:]:
                if (prod.text.startswith(title)):
                    print('찾았다 : ' + title)
                    print("순위 :", (i+j))
                    ActionChains(self.driver).move_to_element(prod).perform()
                    prod.send_keys(Keys.ENTER)
                    isClicked = True
                    break
                j += 1
            i = len(prods)-1

            if isClicked == True:
                super().delay_n(3)
                self.driver.implicitly_wait(7)
                basket = self.driver.find_elements(By.XPATH, '//*[@id="basket"]')[0]
                basket.click()
                print("장바구니 추가")
                super().delay_n(2)
                break

        super().delay_n(2)