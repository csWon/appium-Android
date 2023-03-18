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
        self.doFunctionList = [self.kyobo_best_v1,
                               ]

    def do(self, keyword, page, n, title, doIdx):
        return self.doFunctionList[doIdx](keyword, page, n, title)

    def kyobo_best_v1(self, keyword, page, n, title):

        rank = 1;

        super().printFuncInfo(self.kyobo_best_v1.__name__, keyword, page, n)
        page = page - 1
        n = n - 1
        self.driver.get(self.url_k_product)
        self.driver.implicitly_wait(7)
        super().delay()

        logging.info('start kyobo')
        isPoped = self.driver.find_elements(By.CLASS_NAME, "btn_burst_close")
        for pop in isPoped:
            pop.click()

        isPoped = self.driver.find_elements(By.CLASS_NAME, "btn_main_pop")
        for pop in isPoped:
            if pop.text == '오늘은 그만보기':
                pop.click()

        # // 돋보기 눌려서 product.kyobobook.co.kr로 진입
        btn1 = self.driver.find_elements(By.CLASS_NAME, 'btn_gnb_search')
        btn1[0].click()

        self.driver.implicitly_wait(7)
        super().delay()

        btn2 = self.driver.find_elements(By.CLASS_NAME, 'btn_header_search')
        if len(btn2) != 0 :
            btn2[0].click()


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
        else:
            self.driver.back()

        mainContent = self.driver.find_elements(By.CLASS_NAME, "welcome_main_content_area")
        ActionChains(self.driver).move_to_element(mainContent[-4]).perform()
        super().delay_n(2)
        mainContent2 = self.driver.find_element(By.ID, "welcome_bestseller")
        ActionChains(self.driver).move_to_element(mainContent2).perform()
        super().delay_n(3)

        best = self.driver.find_element(By.XPATH, '//*[@id="welcome_bestseller"]/div[1]/div/a')
        super().delay_n(2)
        best.send_keys(Keys.ENTER)
        super().delay_n(2)
        self.driver.implicitly_wait(20)
        print("베스트 이동")


        isPoped = self.driver.find_elements(By.CLASS_NAME, "btn_main_pop")
        for pop in isPoped:
            if pop.text == '오늘은 그만보기':
                pop.click()

        i = 0
        isClicked = False

        for page in range(150):
            prods = self.driver.find_elements(By.CLASS_NAME, "prod_info")
            ActionChains(self.driver).move_to_element(prods[-2]).perform()
            j = 0

            for prod in prods[i:]:
                if (prod.text.startswith(title)):
                    print('찾았다 : ' + title)
                    print("순위 :", (i+j))
                    rank = i + j
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

        return {"rank": rank, "func": "kyobo_best_v1", "id": "", "pw": ""};