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
        logging.info('start kyobo')
        print('start kyobo_best_v1')
        # // 돋보기 눌려서 product.kyobobook.co.kr로 진입
        # btn = self.driver.find_element(By.CLASS_NAME, 'btn_gnb_search')
        btn = self.driver.find_element(By.XPATH, '//*[@id="mainDiv"]/header/div[3]/a[1]')
        btn.click()
        #
        # # btn_header_search
        # btn = driver.find_element(By.CLASS_NAME, 'btn_header_search')
        # btn.click()
        #
        # # // 검색하기 전 단계로 진입하기
        # search_box = driver.find_element(By.CLASS_NAME, 'btn_header_search')

        # search_box = driver.find_element(By.CLASS_NAME, 'ip_gnb_search')
        # search_box.send_keys('사국지')
        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=2)

        super().delay()
        for fkeyword in Keyword_3:
             # 검색창 클릭
             print(fkeyword)
             search_box = self.driver.find_element(By.ID, 'searchKeyword')
             search_box.click()
             super().delay()
             search_box.send_keys(fkeyword)
             super().delay()
             btn = self.driver.find_element(By.XPATH, '//*[@id="searchDiv"]/header/div[2]/div/a')
             btn.click()
             super().delay()
             btn = self.driver.find_element(By.XPATH, '//*[@id="mainDiv"]/header/div[2]/div/div/button')
             btn.click()

        # driver.get(url_k_product)
        super().delay_n(3)
        #//*[@id="welcome_header_wrap"]/div[3]/div/div[1]/a
        # logobtn = self.driver.find_element(By.XPATH, '//*[@id="welcome_header_wrap"]/div[3]/div/div[1]/a')
        # logobtn.click()
        self.driver.get(super().url_k_product)
        print("메인 이동")
        super().delay_n(2)
        s = self.driver.find_element(By.XPATH, '//*[@id="contents"]/div[4]/div[2]/div[1]/div/a/span[1]')
        s.click()
        super().delay_n(3)

        # s = driver.find_elements(By.CLASS_NAME, 'prod_info')
        i = 0
        find_target = 0
        endflag = False
        for page in range(2,8):
            targets = self.driver.find_elements(By.CLASS_NAME, 'prod_info')
            for target in targets:
                # logging.info(target.text)
                i = i + 1
                if (target.text == title):
                    find_target = target
                elif (find_target != 0):
                    # target.click()
                    endflag = True
                    ActionChains(self.driver).move_to_element(target).perform()  # .click().perform()
                    find_target.click()
                    logging.info('idx : ' + str(i - 1))
                    logging.info('clicked title : ' + self.driver.title)
                    break
            if endflag == True:
                break
            self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
            # 위쪽
            # '//*[@id="tabRoot"]/div[2]/div[1]/div/a[2]'
            # '//*[@id="tabRoot"]/div[2]/div[1]/div/a[3]'
            # 아래쪽
            # '//*[@id="tabRoot"]/div[4]/div[2]/div/a[2]'
            s = self.driver.find_element(By.XPATH, '//*[@id="tabRoot"]/div[2]/div[1]/div/a['+str(page)+']')
            s.click()
            super().delay()
#        '//*[@id="mainDiv"]/main/section[2]'//*[@id="tabRoot"]/div[2]/div[1]/div/a[3]



        # for i in range(1,3):
        #     for j in range(1,11):
        #         product = driver.find_element(By.XPATH, '//*[@id="tabRoot"]/div[4]/ol['+ str(i) +']/li['+ str(j) +']/div[2]/div[2]/a')
        #         if(product.text == title):
        #             product.click()
        #             print('idx : ' + str((10*(i-1))+j))

        # for i in range(1, 5):
        #     tryPage = page-1+i
        #     print("tryPage " + str(tryPage+1))
        #     btn = driver.find_elements(By.CLASS_NAME, 'btn_page_num')
        #     btn[tryPage].click()
        #     delay()
        #
        #     # 물건 클릭
        #     elements = driver.find_elements(By.CLASS_NAME, 'prod_info')
        #     target = getTargetElement(elements, title)
        #     if target == 'empty':
        #         continue
        #     else:
        #         print("clickPage" + str(tryPage+1))
        #         target.click()
        #         break

        self.driver.implicitly_wait(20)
        # targetProduct = driver.find_element(By.CLASS_NAME, 'prod_info')
        # targetProduct = driver.find_elements(By.CLASS_NAME, 'prod_link')
        # targetProduct[n].click()
        # driver.find_element_by_xpath('//*[@class="prod_link"]').send_keys(Keys.ENTER)
        # targetProduct.click()
        # targetProduct.send_keys(Keys.ENTER)
        super().delay_n(60)

    def kyobo_v2(self, keyword, page, n, title):
        super().printFuncInfo(self.kyobo_v2.__name__, keyword, page, n)
        page = page - 1
        n = n - 1
        self.driver.get(super().url_k_product)
        print('start kyobo')
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
            print("tryPage " + str(tryPage + 1))
            btn = self.driver.find_elements(By.CLASS_NAME, 'btn_page_num')
            btn[tryPage].click()
            super().delay()

            # 물건 클릭
            elements = self.driver.find_elements(By.CLASS_NAME, 'prod_info')
            target = super().getTargetElement(elements, title)
            if target == 'empty':
                continue
            else:
                print("clickPage" + str(tryPage + 1))
                target.click()
                break

        self.driver.implicitly_wait(20)
        # targetProduct = driver.find_element(By.CLASS_NAME, 'prod_info')
        # targetProduct = driver.find_elements(By.CLASS_NAME, 'prod_link')
        # targetProduct[n].click()
        # driver.find_element_by_xpath('//*[@class="prod_link"]').send_keys(Keys.ENTER)
        # targetProduct.click()
        # targetProduct.send_keys(Keys.ENTER)
        print(self.driver.title)
        print(self.driver.current_url)
        super().delay_n(60)
