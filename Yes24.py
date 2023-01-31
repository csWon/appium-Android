from BookStore import bookStore
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random

class yes24(bookStore):
    def __init__(self, driver):
        # bookStore.__init__(self)
        self.driver = driver

    def do(self, keyword, page, n, title):
        self.yes24_best_phone(keyword, page, n, title)

    def yes24_best_phone(self, keyword, page, n, title):
        super().printFuncInfo(self.yes24_best_phone.__name__, keyword, page, n)

        self.driver.get('http://www.yes24.com/')

        close_popup_btn = self.driver.find_element(By.XPATH, '//*[@id="yesBotImgPop"]/div/div/div[3]/ul/li[2]/a')
        close_popup_btn.click()

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=2)
        for fKeyword in Keyword_3:
            try:
                # 책 제목 입력
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.ID, 'query')
                search_box.click()
                search_box.send_keys(fKeyword)
                super().delay()
                logging.info(fKeyword)

                # 검색 버튼 클릭
                # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
                btn = self.driver.find_element(By.CLASS_NAME, 'btn_ad_search')
                btn.click()
                super().delay_10()

                # document.getElementsByClassName('yesUI_pagen')[1].children[4].click()
                # document.getElementsByClassName('gd_name')[10].text
                targets = self.driver.find_elements(By.CLASS_NAME, 'lnk_img')
                # targets[10].click()
                targets[1].click()
                super().delay_n(3)

                # targets = driver.find_elements(By.CLASS_NAME, 'btnC m_size btn_blue')
                # targets[0].click()
                targets = self.driver.find_element(By.ID, 'addToCartForDetail')
                targets.click()
                super().delay_n(3)

                # targets = driver.find_elements(By.CLASS_NAME, 'bgYUI btn_popClose')
                # targets = driver.find_elements(By.CLASS_NAME, 'popYUI_close')
                #  targets[4].click()
                s = self.driver.find_element(By.XPATH, '//*[@id="dPop_cartWide"]/div/div/div[4]')
                s.click()
                super().delay_n(3)

                self.driver.back()
                super().delay_n(3)
                self.driver.back()
                super().delay_n(3)
            except Exception as e:
                logging.info("loop exception!! : ", e)

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="yesFixCorner"]/dl/dd/ul[1]/li[1]/a')
        bestBtn.click()
        # search_box.send_keys(keyword)
        # delay()

        # 첫 페이지에서 검색
        for i in range(1, 41):
            product = self.driver.find_element(By.XPATH, '//*[@id="bestList"]/ol/li[' + str(i) + ']/p[3]/a')
            if (product.text == title):
                product.click()
                logging.info('idx : ' + str(i))
                logging.info(self.driver.current_url)
                logging.info('clicked title : ' + self.driver.title)
                super().delay_n(60)
                return

        nextPage = self.driver.find_element(By.XPATH, '//*[@id="bestList"]/p[2]/a/img')
        nextPage.click()

        # 두 번째 페이지 이후부터 검색
        for page in range(3, 10):
            for i in range(0, 40):
                product = self.driver.find_elements(By.XPATH, '//*[@id="category_layout"]/tbody/tr[' + str(
                    1 + i * 2) + ']/td[2]/div/a/img')

                if (product[0].accessible_name == title):
                    product[0].click()
                    logging.info('idx : ' + str(i + ((page - 2) * 40)) + 1)
                    logging.info(self.driver.current_url)
                    logging.info('clicked title : ' + self.driver.title)
                    super().delay_n(60)
                    return
            nextPage = self.driver.find_element(By.XPATH,
                                                '//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[' + str(page + 1) + ']')
            nextPage.click()




    def yes24_best_v1(self, keyword, page, n, title):
        super().printFuncInfo(self.yes24_best_v1.__name__, keyword, page, n)
        n = n + 1

        self.driver.get('http://www.yes24.com/')

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=2)
        for fKeyword in Keyword_3:
            try:
                # 책 제목 입력
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.CLASS_NAME, 'iptTxt')
                search_box.click()
                search_box.send_keys(fKeyword)
                super().delay()
                logging.info(fKeyword)

                # 검색 버튼 클릭
                # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
                btn = self.driver.find_element(By.CLASS_NAME, 'schBtn')
                btn.click()
                super().delay_10()

                # document.getElementsByClassName('yesUI_pagen')[1].children[4].click()
                # document.getElementsByClassName('gd_name')[10].text
                targets = self.driver.find_elements(By.CLASS_NAME, 'lnk_img')
                # targets[10].click()
                targets[1].click()
                super().delay_n(3)

                # targets = driver.find_elements(By.CLASS_NAME, 'btnC m_size btn_blue')
                # targets[0].click()
                targets = self.driver.find_element(By.ID, 'addToCartForDetail')
                targets.click()
                super().delay_n(3)

                # targets = driver.find_elements(By.CLASS_NAME, 'bgYUI btn_popClose')
                # targets = driver.find_elements(By.CLASS_NAME, 'popYUI_close')
                #  targets[4].click()
                s = self.driver.find_element(By.XPATH, '//*[@id="dPop_cartWide"]/div/div/div[4]')
                s.click()
                super().delay_n(3)

                self.driver.back()
                super().delay_n(3)
                self.driver.back()
                super().delay_n(3)
            except Exception as e:
                logging.info("loop exception!! : ", e)

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="yesFixCorner"]/dl/dd/ul[1]/li[1]/a')
        bestBtn.click()
        # search_box.send_keys(keyword)
        # delay()

        # 첫 페이지에서 검색
        for i in range(1, 41):
            product = self.driver.find_element(By.XPATH, '//*[@id="bestList"]/ol/li[' + str(i) + ']/p[3]/a')
            if (product.text == title):
                product.click()
                logging.info('idx : ' + str(i))
                logging.info(self.driver.current_url)
                logging.info('clicked title : ' + self.driver.title)
                super().delay_n(60)
                return

        nextPage = self.driver.find_element(By.XPATH, '//*[@id="bestList"]/p[2]/a/img')
        nextPage.click()

        #두 번째 페이지 이후부터 검색
        for page in range(3, 10):
            for i in range(0, 40):
                product = self.driver.find_elements(By.XPATH, '//*[@id="category_layout"]/tbody/tr[' + str(1 + i * 2) + ']/td[2]/div/a/img')

                if (product[0].accessible_name == title):
                    product[0].click()
                    logging.info('idx : ' + str(i+((page-2)*40))+1)
                    logging.info(self.driver.current_url)
                    logging.info('clicked title : ' + self.driver.title)
                    super().delay_n(60)
                    return
            nextPage = self.driver.find_element(By.XPATH, '//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a['+str(page+1)+']')
            nextPage.click()

#
# '//*[@id="category_layout"]/tbody/tr[3]/td[2]/div/a/img'
# '//*[@id="category_layout"]/tbody/tr[5]/td[2]/div/a/img'
# '//*[@id="category_layout"]/tbody/tr[7]/td[2]/div/a[1]/img'
# '//*[@id="category_layout"]/tbody/tr[9]/td[2]/div/a[1]/img'
        # product = self.driver.find_element(By.XPATH, '//*[@id="bestList"]/ol/li[' + str(i) + ']/p[3]/a')
        # product.click()

# '//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[4]' # 3page
# '//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[5]' # 4page
