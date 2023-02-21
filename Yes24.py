from BookStore import bookStore
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import datetime
import time

class yes24(bookStore):
    def __init__(self, driver):
        # bookStore.__init__(self)
        self.driver = driver
        self.rank = 0
        self.doFunctionList = [self.yes24_best_phone,
                               ]
    def doScrollDown(self, whileSeconds):
        SCROLL_PAUSE_SEC = 1
        # 스크롤 높이 가져옴
        last_height = 0#self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, whileSeconds):
            last_height = last_height + 200
            self.driver.execute_script("window.scrollTo(0, " + str(last_height) + ");")
            # 1초 대기
            time.sleep(SCROLL_PAUSE_SEC)

    def do(self, keyword, page, n, title, doIdx):
        return self.doFunctionList[doIdx](keyword, page, n, title)

    def yes24_best_phone(self, keyword, page, n, title):
        super().printFuncInfo(self.yes24_best_phone.__name__, keyword, page, n)


        self.driver.get('http://www.yes24.com/')
        self.driver.delete_all_cookies()

        close_popup_btn = self.driver.find_element(By.XPATH, '//*[@id="yesAppPop"]/div/div/div[2]')
        close_popup_btn.click()
        super().delay()

        close_popup_btn = self.driver.find_element(By.XPATH, '//*[@id="yesBotImgPop"]/div/div/div[3]/ul/li[1]/a')
        close_popup_btn.click()
        super().delay()

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=1)
        for fKeyword in Keyword_3:
            try:
                print(fKeyword)
                # close_popup_btn = self.driver.find_element(By.XPATH, '//*[@id="yesBotImgPop"]/div/div/div[3]/ul/li[1]/a')
                # close_popup_btn.click()
                # super().delay()

                # 책 제목 입력
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.ID, 'query')
                search_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                search_box.click()
                search_box.send_keys(fKeyword)
                super().delay()
                logging.info(fKeyword)

                # 검색 버튼 클릭
                # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
                btn = self.driver.find_element(By.ID, 'search_real_search')
                btn.click()
                super().delay()

                # document.getElementsByClassName('yesUI_pagen')[1].children[4].click()
                # document.getElementsByClassName('gd_name')[10].text
                targets = self.driver.find_elements(By.CLASS_NAME, 'lnk_item')

                # target_image = self.driver.find_element(By.XPATH, '//*[@id="yesSchGList"]/li[2]/div/div[1]/div[1]/span/span/em/img')
                # target_image_src = target_image.get_attribute('src')
                #
                # # 물건이 19금이면 로그인이 필요해서 예외처리 추가
                # if 'PD_19_L.gif' in target_image_src:
                #     continue
                # # targets[10].click()
                targets[1].click()

                # try:
                #     self.driver.switchTo().alert();
                #     self.driver.findElement(By.name, 'OK').click();
                #     t = self.driver.find_elements(By.ID, 'SMemberID')
                #     if len(t) != 0:
                #         continue
                # except:
                #     a = 0 # 19금 아닌경우 여기로 빠지고 아래 코드 계속 수행



                super().delay_n(3)

                # btnDes에 스트링 분철신청 가능 등 문자가 있는경우 예외처리를 위해서 확인
                flag = False
                targets = self.driver.find_elements(By.CLASS_NAME, 'btnDes')
                self.driver.implicitly_wait(5)
                if len(targets) > 0:
                    flag = True

                try:
                    btns_addcart = self.driver.find_elements(By.CLASS_NAME, 'btn_c.btn_blue')
                    for btn in btns_addcart:
                        if btn.text == '카트에 넣기':
                            btn.click()

                            super().delay()

                            # targets = driver.find_elements(By.CLASS_NAME, 'bgYUI btn_popClose')
                            # targets = driver.find_elements(By.CLASS_NAME, 'popYUI_close')
                            #  targets[4].click()

                            if flag:
                                btn.click()
                            btn_addcart_x = self.driver.find_element(By.XPATH, '//*[@id="yesWrap"]/div[7]/div/div/div/div/div[2]/a[2]')
                            btn_addcart_x.click()
                            super().delay()

                            self.driver.back()
                            super().delay_n(3)
                            break;
                except:
                    continue

                self.driver.back()
                super().delay_n(3)
            except Exception as e:
                logging.info("loop exception!! : ", e)
        # '//*[@id="hd"]/div/h1'
        logoBtn = self.driver.find_element(By.XPATH, '//*[@id="hd"]/div/h1')
        logoBtn.click()

        # self.driver.back()
        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()
        # search_box.send_keys(keyword)
        # delay()

        # 첫 페이지에서 검색
        for i in range(1, 51):
            # '//*[@id="bestSellerList"]/li[1]/div/div[2]/div[1]'
            # '//*[@id="bestSellerList"]/li[2]/div/div[2]/div[1]'
            # '//*[@id="bestSellerList"]/li[1]/div/div[2]/div[1]'
            # '//*[@id="bestSellerList"]/li[1]/div/a'
            product = self.driver.find_element(By.XPATH, '//*[@id="bestSellerList"]/li[' + str(i) + ']/div/div[2]/div[1]')
            if (product.text == title):
                product = self.driver.find_element(By.XPATH, '//*[@id="bestSellerList"]/li['+str(i)+']/div/a')
                product_next = self.driver.find_element(By.XPATH, '//*[@id="bestSellerList"]/li[' + str(i+1) + ']/div/a')
                ActionChains(self.driver).move_to_element(product_next).perform()  # .click().perform()
                product.click()
                print('idx : ' + str(i))
                self.rank = i
                print('clicked title : ' + self.driver.title)
                # logging.info('idx : ' + str(i))
                # logging.info(self.driver.current_url)
                # logging.info('clicked title : ' + self.driver.title)
                # super().delay_n(10)
                try:
                    btns_addcart = self.driver.find_elements(By.CLASS_NAME, 'btn_c.btn_blue')
                    for btn in btns_addcart:
                        if btn.text == '카트에 넣기':
                            btn.click()

                            super().delay()

                            # targets = driver.find_elements(By.CLASS_NAME, 'bgYUI btn_popClose')
                            # targets = driver.find_elements(By.CLASS_NAME, 'popYUI_close')
                            #  targets[4].click()
                            btn_addcart_x = self.driver.find_element(By.XPATH, '//*[@id="yesWrap"]/div[7]/div/div/div/div/div[2]/a[2]')
                            btn_addcart_x.click()
                            super().delay()

                            break;
                except:
                    return self.rank
                self.doScrollDown(30)

                return self.rank

        return self.rank
        # nextPage = self.driver.find_element(By.XPATH, '//*[@id="bestSeller50More"]/a')
        # nextPage.click()

        # # 두 번째 페이지 이후부터 검색
        # for page in range(3, 10):
        #     for i in range(0, 40):
        #         product = self.driver.find_elements(By.XPATH, '//*[@id="category_layout"]/tbody/tr[' + str(
        #             1 + i * 2) + ']/td[2]/div/a/img')
        #
        #         if (product[0].accessible_name == title):
        #             product[0].click()
        #             logging.info('idx : ' + str(i + ((page - 2) * 40)) + 1)
        #             logging.info(self.driver.current_url)
        #             logging.info('clicked title : ' + self.driver.title)
        #             super().delay_n(60)
        #             return
        #     nextPage = self.driver.find_element(By.XPATH,
        #                                         '//*[@id="bestList"]/div[3]/div[1]/div[1]/p/a[' + str(page + 1) + ']')
        #     nextPage.click()




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
