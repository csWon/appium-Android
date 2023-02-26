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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class yes24(bookStore):
    def __init__(self, driver):
        # bookStore.__init__(self)
        self.driver = driver
        self.rank = 0
        self.doFunctionList = [self.yes24_best_phone,
                               self.yes24_best_phone1,
                               self.yes24_best_phone2,
                               self.yes24_best_phone3,
                               self.yes24_best_phone4,
                               self.yes24_best_phone5,
                               self.yes24_best_phone6,
                               ]
        self.driver.get('http://www.yes24.com/')
        self.driver.delete_all_cookies()

    def doScrollDown(self, whileSeconds):
        SCROLL_PAUSE_SEC = 1
        # 스크롤 높이 가져옴
        last_height = 0#self.driver.execute_script("return document.body.scrollHeight")

        for i in range(0, whileSeconds):
            num = random.choices(range(0, 9), k=1)
            if num[0] <7:
                last_height = last_height + 200
            else:
                last_height = last_height - 200
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
        ActionChains(self.driver).move_to_element(logoBtn).perform()  # .click().perform()
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



    def bookOfMonthClick(self, delay_s):
        btn = self.driver.find_element(By.XPATH, '//*[@id="main_top_area"]/div[2]/ul/li[9]/a/em[1]/img')
        btn.click()
        self.doScrollDown(delay_s)
        homeBtn = self.driver.find_element(By.ID, 'Layer_1')
        homeBtn.click()
    def bookOfTodayClick(self, delay_s):
        btns = self.driver.find_elements(By.CLASS_NAME, 'tBook_img')

        for btn in btns:
            if EC.element_to_be_clickable(btn):
                btn.send_keys(Keys.ENTER)
                break
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "tBook_img"))
        # )

        self.doScrollDown(delay_s)
        homeBtn = self.driver.find_element(By.ID, 'Layer_1')
        homeBtn.click()

    # def realtimeBookUpClick(self, delay_s):
    #     tit_txts = self.driver.find_elements(By.CLASS_NAME, 'tit_txt')
    #
    #     target = ''
    #     for tit_txt in tit_txts:
    #         if tit_txt.text == '실시간 BOOK UP!':
    #             target = tit_txt
    #             break
    #
    #     ActionChains(self.driver).move_to_element(target).perform()  # .click().perform()
    #     target.click()
    #
    #     self.doScrollDown(delay_s)
    #     self.driver.find_element(By.ID, 'Layer_1')

    def shortCutClick(self, delay_s):
        btn = self.driver.find_elements(By.XPATH, '//*[@id="main_top_area"]/div[2]/ul/li[1]/a')
        btn.click()
        self.doScrollDown(delay_s)
        self.goToHome()

    def hotBookClick(self, delay_s):
        btn = self.driver.find_elements(By.CLASS_NAME, 'lnk_hHot')
        ActionChains(self.driver).move_to_element(btn[2]).perform()
        btn[0].click()

        self.doScrollDown(delay_s)
        self.goToHome()

    def bannerClick(self, delay_s):

        for i in range(0, 8):
            try:
                btn = self.driver.find_element(By.XPATH, '//*[@id="adPubBestF"]/div/div/div['+str(i)+']')
                btn.click()
                break
            except WebDriverException:
                a=0
        self.doScrollDown(delay_s)
        self.goToHome()

    def goToHome(self):
        homeBtn = self.driver.find_element(By.ID, 'Layer_1')
        ActionChains(self.driver).move_to_element(homeBtn).perform()
        homeBtn.click()

    def routineAfterClickBook(self, delay_s):

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

                    if flag:
                        btn.click()
                    btn_addcart_x = self.driver.find_element(By.XPATH,
                                                             '//*[@id="yesWrap"]/div[7]/div/div/div/div/div[2]/a[2]')
                    btn_addcart_x.click()
                    super().delay()
                    self.doScrollDown(delay_s)
                    self.driver.back()

                    break;
        except:
            return -1

        self.driver.back()
        super().delay_n(2)










    def clickTargetBook(self, keyword, delay_s):
        search_box = self.driver.find_element(By.ID, 'query')
        search_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        search_box.click()
        search_box.send_keys(keyword)
        super().delay()
        logging.info(keyword)

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
        targets[0].click()
        self.routineAfterClickBook(delay_s)

        return 0

    def clickBookInBest(self, title, targetDelay):
        # best 1~100에서 검색
        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()

        for j in range(0,2):
            for i in range(1, 51):
                targetIdx = i + (j*50)

                product = self.driver.find_element(By.XPATH,
                                                   '//*[@id="bestSellerList"]/li[' + str(targetIdx) + ']/div/div[2]/div[1]')
                if (product.text == title):
                    product = self.driver.find_element(By.XPATH, '//*[@id="bestSellerList"]/li[' + str(targetIdx) + ']/div/a')
                    product_next = self.driver.find_element(By.XPATH,
                                                            '//*[@id="bestSellerList"]/li[' + str(targetIdx + 1) + ']/div/a')
                    ActionChains(self.driver).move_to_element(product_next).perform()  # .click().perform()
                    product.click()
                    print('idx : ' + str(targetIdx))
                    self.rank = targetIdx
                    print('clicked title : ' + self.driver.title)
                    # logging.info('idx : ' + str(i))
                    # logging.info(self.driver.current_url)
                    # logging.info('clicked title : ' + self.driver.title)
                    # super().delay_n(10)
                    self.routineAfterClickBook(delay_s=targetDelay)

                    return self.rank

            if j == 0:
                nextBtn = self.driver.find_element(By.ID, 'bestSeller50More')  # 베스트셀러 50개 더 보기
                footer = self.driver.find_element(By.ID, 'footer')
                ActionChains(self.driver).move_to_element(footer).perform()
                self.delay()
                nextBtn.click()
            elif j == 1:
                nextBtn = self.driver.find_element(By.ID, 'bestSellerYMore')  # 베스트셀러 전체 더 보기
                footer = self.driver.find_element(By.ID, 'footer')
                ActionChains(self.driver).move_to_element(footer).perform()
                self.delay()
                nextBtn.click()

                # 바뀐 포멧에서 1페이지부터 34페이지까지 순회 시작
                # 한 스텝 당 5페이지로 구성
                # 1-5page   step 1
                # 6-10  step 2
                # ...
                # 31-34  step 7
                rank = 0
                for step in range(0,7):
                    offset = 0
                    if step != 0:
                        offset = 2

                    for page in range(1, 6):

                        for i in range(1, 31):
                            productName = self.driver.find_element(By.XPATH,
                                                                   '//*[@id="yGoodsList"]/li[' + str(i) + ']/div[1]/div/p[1]')
                            if productName.text.strip() == title:
                                product = self.driver.find_element(By.XPATH,
                                                                   '//*[@id="yGoodsList"]/li[' + str(i) + ']/div[1]/a[1]')
                                product.click()
                                self.routineAfterClickBook(targetDelay)
                                self.rank = step * 150 + (page - 1) * 30 + i
                                return
                        pageBtn = self.driver.find_element(By.XPATH, '//*[@id="pager"]/a[' + str(page + offset) + ']')
                        ActionChains(self.driver).move_to_element(pageBtn).send_keys(Keys.PAGE_DOWN).perform()

                        self.delay()
                        pageBtn.click()
                        self.delay()
        return

    def closePopups(self):
        close_popup_btn = self.driver.find_element(By.XPATH, '//*[@id="yesAppPop"]/div/div/div[2]')
        close_popup_btn.click()
        super().delay()

        close_popup_btn = self.driver.find_element(By.XPATH, '//*[@id="yesBotImgPop"]/div/div/div[3]/ul/li[1]/a')
        close_popup_btn.click()
        super().delay()

    def searchFakeKeywords(self, fkeywordCnt, fkeywordDelay):
        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=fkeywordCnt)

        for fKeyword in Keyword_3:
            try:
                print(fKeyword)
                ret = self.clickTargetBook(fKeyword, fkeywordDelay)
                if ret == -1:
                    continue
            except Exception as e:
                logging.info("loop exception!! : ", e)

    def yes24_best_phone1(self, keyword, page, n, title):
        #111
        #110
        #101
        #011
        #100
        #001

        fkeywordDelay = 20
        targetDelay = 60
        fkeywordCnt = 2

        super().printFuncInfo(self.yes24_best_phone1.__name__, keyword, page, n)

        self.closePopups()

        # self.bookOfTodayClick(delay_s=5)
        self.bookOfMonthClick(delay_s=5)
        self.hotBookClick(delay_s=5)

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        logoBtn = self.driver.find_element(By.XPATH, '//*[@id="hd"]/div/h1')
        ActionChains(self.driver).move_to_element(logoBtn).perform()  # .click().perform()
        logoBtn.click()

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()

        self.bannerClick(delay_s=fkeywordDelay)

        # self.clickBookInBest(title, targetDelay)
        self.clickTargetBook(title, targetDelay)

        return self.rank


    def yes24_best_phone2(self, keyword, page, n, title):
        fkeywordDelay = 20
        targetDelay = 60
        fkeywordCnt = 2

        super().printFuncInfo(self.yes24_best_phone2.__name__, keyword, page, n)

        self.closePopups()

        # self.bookOfTodayClick(delay_s=5)
        self.bookOfMonthClick(delay_s=5)
        self.hotBookClick(delay_s=5)

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        logoBtn = self.driver.find_element(By.XPATH, '//*[@id="hd"]/div/h1')
        ActionChains(self.driver).move_to_element(logoBtn).perform()  # .click().perform()
        logoBtn.click()

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()

        # self.bannerClick(delay_s=fkeywordDelay)

        # self.clickBookInBest(title, targetDelay)
        self.clickTargetBook(title, targetDelay)

        return self.rank


    def yes24_best_phone3(self, keyword, page, n, title):
        fkeywordDelay = 20
        targetDelay = 60
        fkeywordCnt = 2

        super().printFuncInfo(self.yes24_best_phone3.__name__, keyword, page, n)

        self.closePopups()

        # self.bookOfTodayClick(delay_s=5)
        self.bookOfMonthClick(delay_s=5)
        # self.hotBookClick(delay_s=5)

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        logoBtn = self.driver.find_element(By.XPATH, '//*[@id="hd"]/div/h1')
        ActionChains(self.driver).move_to_element(logoBtn).perform()  # .click().perform()
        logoBtn.click()

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()

        self.bannerClick(delay_s=fkeywordDelay)

        # self.clickBookInBest(title, targetDelay)
        self.clickTargetBook(title, targetDelay)

        return self.rank


    def yes24_best_phone4(self, keyword, page, n, title):
        fkeywordDelay = 20
        targetDelay = 60
        fkeywordCnt = 2

        super().printFuncInfo(self.yes24_best_phone4.__name__, keyword, page, n)

        self.closePopups()

        # self.bookOfTodayClick(delay_s=5)
        self.bookOfMonthClick(delay_s=5)
        self.hotBookClick(delay_s=5)

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        logoBtn = self.driver.find_element(By.XPATH, '//*[@id="hd"]/div/h1')
        ActionChains(self.driver).move_to_element(logoBtn).perform()  # .click().perform()
        logoBtn.click()

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()

        # self.bannerClick(delay_s=fkeywordDelay)

        # self.clickBookInBest(title, targetDelay)
        self.clickTargetBook(title, targetDelay)

        return self.rank



    def yes24_best_phone5(self, keyword, page, n, title):
        fkeywordDelay = 20
        targetDelay = 60
        fkeywordCnt = 2

        super().printFuncInfo(self.yes24_best_phone5.__name__, keyword, page, n)

        self.closePopups()

        # self.bookOfTodayClick(delay_s=5)
        self.bookOfMonthClick(delay_s=5)
        self.hotBookClick(delay_s=5)

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        logoBtn = self.driver.find_element(By.XPATH, '//*[@id="hd"]/div/h1')
        ActionChains(self.driver).move_to_element(logoBtn).perform()  # .click().perform()
        logoBtn.click()

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()

        self.bannerClick(delay_s=fkeywordDelay)

        self.clickBookInBest(title, targetDelay)
        # self.clickTargetBook(title, targetDelay)

        return self.rank


    def yes24_best_phone6(self, keyword, page, n, title):
        fkeywordDelay = 20
        targetDelay = 60
        fkeywordCnt = 2

        super().printFuncInfo(self.yes24_best_phone5.__name__, keyword, page, n)

        self.closePopups()

        # self.bookOfTodayClick(delay_s=5)
        self.bookOfMonthClick(delay_s=5)
        # self.hotBookClick(delay_s=5)

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        logoBtn = self.driver.find_element(By.XPATH, '//*[@id="hd"]/div/h1')
        ActionChains(self.driver).move_to_element(logoBtn).perform()  # .click().perform()
        logoBtn.click()

        bestBtn = self.driver.find_element(By.XPATH, '//*[@id="welcomeMenu_3"]')
        bestBtn.click()

        self.bannerClick(delay_s=fkeywordDelay)

        self.clickBookInBest(title, targetDelay)
        # self.clickTargetBook(title, targetDelay)

        return self.rank


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
