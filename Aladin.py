from BookStore import bookStore
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string
import time

class aladin(bookStore):
    def __init__(self, driver):
        # bookStore.__init__(self)
        self.driver = driver
        self.rank = 0
        self.doFunctionList = [self.aladin_best_phone_v1,
                               self.aladin_best_phone_v2,
                               self.aladin_best_phone_v3,
                           ]
        self.driver.get(self.url_aladin)

    def do(self, keyword, page, n, title, doIdx):
        # try:
        self.doFunctionList[doIdx](keyword, page, n, title)
        return self.rank
        # except Exception as e:
        #     print("do exception!! : ", e)
    def doScrollDown(self, whileSeconds):
        SCROLL_PAUSE_SEC = 1
        # 스크롤 높이 가져옴
        last_height = 0#self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, whileSeconds):
            last_height = last_height + 200
            self.driver.execute_script("window.scrollTo(0, " + str(last_height) + ");")
            # 1초 대기
            time.sleep(SCROLL_PAUSE_SEC)
    def aladin_best_v1(self, keyword, page, n, title):
        super().printFuncInfo(self.aladin_best_v1.__name__, keyword, page, n)
        page = page - 2
        n = n - 1
        self.driver.get(super().url_aladin)
        # 책 제목 입력
        bestbtn = self.driver.find_element(By.XPATH, '//*[@id="re_mallmenu"]/ul/li[3]/div/a/img')
        bestbtn.click()
        super().delay()

        i = 0;

        endflag = False
        for _page in range(3,8):
            targets = self.driver.find_elements(By.CLASS_NAME, 'bo3')
            super().delay()
            for target in targets:
                # logging.info(target.text)
                i = i + 1
                if (target.text == title):
                    endflag=True
                    target.click()
                    logging.info('idx : ' + str(i))
                    logging.info(self.driver.current_url)
                    logging.info('clicked title : ' + self.driver.title)
                    break
            if endflag == True:
                break
            nextPageBtn = self.driver.find_element(By.XPATH, '//*[@id="newbg_body"]/div[3]/ul/li['+str(_page)+']/a')
            nextPageBtn.click()
            super().delay()

        super().delay_n(20)

    def inputTextBox(self, id, text):
        nm_box = self.driver.find_element(By.ID, id)
        nm_box.send_keys(text)
        super().delay_n(3)

    def simple_join(self):
        names = open('nameDB.txt', 'r', encoding='UTF8').read().split('\n')
        nm = random.choices(names, k=1)
        self.inputTextBox('CustomerName', nm)

        CustId = string.ascii_lowercase
        CustId = ''.join(random.choice(CustId) for i in range(10))
        self.inputTextBox('CustId', CustId)

        email = string.ascii_lowercase
        email = ''.join(random.choice(email) for i in range(10))
        self.inputTextBox('Email', email)

        self.inputTextBox('EmailDomainText', 'naver.com')

        pw_string  = string.ascii_lowercase
        pw_string = ''.join(random.choice(pw_string) for i in range(5))
        pw_digit = string.digits
        pw_digit = ''.join(random.choice(pw_digit) for i in range(5))
        self.inputTextBox('password', pw_string + str(pw_digit))
        self.inputTextBox('PasswordVerify', pw_string + str(pw_digit))

        hp2 = string.digits
        hp2 = ''.join(random.choice(hp2) for i in range(4))
        hp3 = string.digits
        hp3 = ''.join(random.choice(hp3) for i in range(4))
        self.inputTextBox('hp1', '010')
        self.inputTextBox('hp2', hp2)
        self.inputTextBox('hp3', hp3)

        checkBox = self.driver.find_element(By.ID, 'agrStipulationAll')
        checkBox.click()

        join_btn = self.driver.find_element(By.ID, 'btn-submit')
        join_btn.click()


    def aladin_best_v3(self, keyword, page, n, title):
        super().printFuncInfo(self.aladin_best_v3.__name__, keyword, page, n)
        page = page - 2
        n = n - 1

        self.driver.get(super().url_aladin)

        simple_join_btn = self.driver.find_element(By.CLASS_NAME, 'set3m')
        simple_join_btn.click()

        self.simple_join()

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=2)
        Keyword_3.append(title)
        for fKeyword in Keyword_3:
            try:
                # 책 제목 입력
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.ID, 'SearchWord')
                search_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                search_box.click()
                search_box.send_keys(fKeyword)
                super().delay()

                # 검색 버튼 클릭
                # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
                btn = self.driver.find_element(By.CLASS_NAME, 'searchBtn')
                btn.click()
                super().delay_10()

                addCartBtn = self.driver.find_element(By.XPATH, '//*[@id="Search3_Result"]/div[1]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]/div/div[1]/a')
                addCartBtn.click()

            except Exception as e:
                logging.info("loop exception!! : ", e)

        bestbtn = self.driver.find_element(By.XPATH, '//*[@id="re_mallmenu"]/ul/li[3]/div/a/img')
        bestbtn.click()
        super().delay()

        i = 0
        endflag = False
        for _page in range(3, 9):
            targets = self.driver.find_elements(By.CLASS_NAME, 'bo3')
            super().delay()
            for target in targets:
                # logging.info(target.text)
                i = i + 1
                if (target.text == title):
                    endflag = True
                    target.click()
                    logging.info('idx : ' + str(i))
                    logging.info(self.driver.current_url)
                    logging.info('clicked title : ' + self.driver.title)
                    addCartBtn = self.driver.find_element(By.CLASS_NAME, 'Ere_btn_cart.Ere_floatL')
                    addCartBtn.click()
                    super().delay()

                    saveBoxBtn = self.driver.find_element(By.ID, 'btn_savebasket')
                    saveBoxBtn.click()
                    super().delay()
                    # btn_buy = self.driver.find_element(By.CLASS_NAME, 'Ere_btn_buyitnow.Ere_floatL.Ere_ML4')
                    # btn_buy.click()
                    # super().delay()
                    #
                    #<div id="btn_savebasket" class="Ere_btn_gift Ere_floatL Ere_ML4 btn_savebasket"><a href="javascript:void(0)" onclick="javascript:SafeBasket_Add();">보관함 +</a><div id="layer_savebasket" class="Ere_layerst_list" style="position: absolute; background-color: white; z-index: 999; display: none;"><ul><li><a href="javascript:SafeBasket_Add(&quot;&quot;);" style="color:#333;font-weight:normal;padding:10px 18px;">보관함</a></li><li><a href="javascript:MyList_Add(&quot;&quot;);" style="color:#333;font-weight:normal;padding:10px 18px;">마이리스트</a></li></ul></div></div>
                    # simple_join_btn = self.driver.find_element(By.CLASS_NAME, 'button_login2')
                    # simple_join_btn.click()

                    # self.simple_join()
                    break
            if endflag == True:
                break
            nextPageBtn = self.driver.find_element(By.XPATH, '//*[@id="newbg_body"]/div[3]/ul/li[' + str(_page) + ']/a')
            nextPageBtn.click()
            super().delay()

        super().delay_n(90)


    def aladin_best_v2(self, keyword, page, n, title):
        super().printFuncInfo(self.aladin_best_v2.__name__, keyword, page, n)
        page = page - 2
        n = n - 1

        self.driver.get(super().url_aladin)

        simple_join_btn = self.driver.find_element(By.CLASS_NAME, 'set3m')
        simple_join_btn.click()

        self.simple_join()

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=2)

        for fKeyword in Keyword_3:
            try:
                # 책 제목 입력
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.ID, 'SearchWord')
                search_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                search_box.click()
                search_box.send_keys(fKeyword)
                super().delay()

                # 검색 버튼 클릭
                # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
                btn = self.driver.find_element(By.CLASS_NAME, 'searchBtn')
                btn.click()
                super().delay_10()

                addCartBtn = self.driver.find_element(By.XPATH, '//*[@id="Search3_Result"]/div[1]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[2]/div/div[1]/a')
                addCartBtn.click()

            except Exception as e:
                print("loop exception!! : ", e)

        bestbtn = self.driver.find_element(By.XPATH, '//*[@id="re_mallmenu"]/ul/li[3]/div/a/img')
        bestbtn.click()
        super().delay()

        i = 0
        endflag = False
        for _page in range(3, 9):
            targets = self.driver.find_elements(By.CLASS_NAME, 'bo3')
            super().delay()
            for target in targets:
                # logging.info(target.text)
                i = i + 1
                if (target.text == title):
                    endflag = True
                    target.click()
                    logging.info('idx : ' + str(i))
                    logging.info(self.driver.current_url)
                    logging.info('clicked title : ' + self.driver.title)
                    addCartBtn = self.driver.find_element(By.CLASS_NAME, 'Ere_btn_cart.Ere_floatL')
                    addCartBtn.click()
                    super().delay()

                    # btn_buy = self.driver.find_element(By.CLASS_NAME, 'Ere_btn_buyitnow.Ere_floatL.Ere_ML4')
                    # btn_buy.click()
                    # super().delay()
                    #
                    #
                    # simple_join_btn = self.driver.find_element(By.CLASS_NAME, 'button_login2')
                    # simple_join_btn.click()

                    # self.simple_join()
                    break
            if endflag == True:
                break
            nextPageBtn = self.driver.find_element(By.XPATH, '//*[@id="newbg_body"]/div[3]/ul/li[' + str(_page) + ']/a')
            nextPageBtn.click()
            super().delay()

        super().delay_n(60)

    def aladin_login(self):
        menuBtn = self.driver.find_element(By.XPATH, '//*[@id="welcom_wrap"]/div[2]/div[2]/a')
        menuBtn.click()
        super().delay()

        joinBtn =  self.driver.find_element(By.XPATH, '//*[@id="aside_top"]/div/div[2]')
        joinBtn.click()
        super().delay()

        checkAcceptAllBtn = self.driver.find_element(By.XPATH, '//*[@id="join_content_in"]/div[1]/div/div[1]/div[3]/div/ul/li/span/label')
        checkAcceptAllBtn.click()
        super().delay()

        nextBtn = self.driver.find_element(By.ID, 'btnAgree')
        nextBtn.click()
        super().delay()

        CustId = string.ascii_lowercase
        CustId = ''.join(random.choice(CustId) for i in range(10))
        self.inputTextBox('CustId', CustId)
        super().delay()

        pw_string  = string.ascii_lowercase
        pw_string = ''.join(random.choice(pw_string) for i in range(5))
        pw_digit = string.digits
        pw_digit = ''.join(random.choice(pw_digit) for i in range(5))
        self.inputTextBox('Password', pw_string + str(pw_digit))
        super().delay()
        self.inputTextBox('PasswordVerify', pw_string + str(pw_digit))
        super().delay()

        nextBtn2 = self.driver.find_element(By.ID, 'btnNext_2')
        nextBtn2.click()
        super().delay()

        names = open('nameDB.txt', 'r', encoding='UTF8').read().split('\n')
        nm = random.choices(names, k=1)
        self.inputTextBox('CustomerName', nm)
        super().delay()

        email = string.ascii_lowercase
        email = ''.join(random.choice(email) for i in range(10))
        self.inputTextBox('Email', email+'@naver.com')
        super().delay()

        # self.inputTextBox('EmailDomainText', 'naver.com')


        hp2 = string.digits
        hp2 = ''.join(random.choice(hp2) for i in range(4))
        hp3 = string.digits
        hp3 = ''.join(random.choice(hp3) for i in range(4))
        self.inputTextBox('cellPhoneNo', '010' + hp2 + hp3)
        super().delay()

        join_btn = self.driver.find_element(By.ID, 'btnJoin')
        join_btn.click()
        super().delay()

        go_to_home_btn = self.driver.find_element(By.XPATH, '//*[@id="join_content_in"]/div[7]/div')
        go_to_home_btn.click()
        super().delay()

    def aladin_best_phone_v1(self, keyword, page, n, title):
        super().printFuncInfo(self.aladin_best_phone_v1.__name__, keyword, page, n)

        # 광고 팝업 끄기
        pop_up_close_btn = self.driver.find_element(By.XPATH, '//*[@id="spaceEventLayer"]/div[1]/a[2]')
        pop_up_close_btn.click()

        self.aladin_login()

        pop_up_close_btn = self.driver.find_element(By.XPATH, '//*[@id="spaceEventLayer"]/div[1]/a[2]')
        pop_up_close_btn.click()

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=1)
        # Keyword_3.append(title)
        for fKeyword in Keyword_3:
            try:
                print(fKeyword)
                # 책 제목 입력을 위한 검색창 클릭
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.ID, 'SearchWordBanner')
                search_box.click()

                search_box2 = self.driver.find_element(By.ID, 'SearchWord')
                search_box2.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                search_box2.click()

                search_box2.send_keys(fKeyword)

                super().delay()

                # 검색 버튼 클릭
                # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
                btn = self.driver.find_element(By.CLASS_NAME, 'sch-go')
                btn.click()
                super().delay_10()

                try:
                    addCartBtn = self.driver.find_element(By.XPATH, '//*[@id="Search3_Result"]/div[4]/table/tbody/tr/td[3]/img')
                    addCartBtn.click()
                    super().delay_n(2)
                    addCartBtn = self.driver.find_element(By.XPATH, '//*[@id="Search3_Result"]/div[4]/div[2]/a[1]')
                    addCartBtn.click()
                except Exception as e:
                    print("do exception!! : ", e)
                    continue

            except Exception as e:
                logging.info("keyword loop exception!! : ", e)

        homebtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/h1')
        homebtn.click()
        super().delay_n(2)

        try:
            pop_up_close_btn = self.driver.find_element(By.XPATH, '//*[@id="spaceEventLayer"]/div[1]/a[2]')
            pop_up_close_btn.click()
        except:
            a = 0
        bestbtn = self.driver.find_element(By.XPATH,'//*[@id="welcom_wrap"]/div[9]/div/li[1]')
        bestbtn.click()
        super().delay()

        i = 0
        endflag = False
        for _page in range(2, 9):
            targets = self.driver.find_elements(By.CLASS_NAME, 'b_book_t')
            super().delay()
            for target in targets:
                # logging.info(target.text)
                i = i + 1
                if title in target.text:
                    endflag = True
                    target.click()
                    self.rank = i
                    print('idx : ' + str(i))
                    logging.info('idx : ' + str(i))
                    logging.info(self.driver.current_url)
                    logging.info('clicked title : ' + self.driver.title)
                    print('clicked title : ' + self.driver.title)
                    addCartBtn = self.driver.find_element(By.ID, 'btnAddBasket')
                    addCartBtn.click()
                    super().delay_n(5)
                    return self.rank

                    # saveBoxBtn = self.driver.find_element(By.ID, 'btn_savebasket')
                    # saveBoxBtn.click()
                    # super().delay()
                    # btn_buy = self.driver.find_element(By.CLASS_NAME, 'Ere_btn_buyitnow.Ere_floatL.Ere_ML4')
                    # btn_buy.click()
                    # super().delay()
                    #
                    #<div id="btn_savebasket" class="Ere_btn_gift Ere_floatL Ere_ML4 btn_savebasket"><a href="javascript:void(0)" onclick="javascript:SafeBasket_Add();">보관함 +</a><div id="layer_savebasket" class="Ere_layerst_list" style="position: absolute; background-color: white; z-index: 999; display: none;"><ul><li><a href="javascript:SafeBasket_Add(&quot;&quot;);" style="color:#333;font-weight:normal;padding:10px 18px;">보관함</a></li><li><a href="javascript:MyList_Add(&quot;&quot;);" style="color:#333;font-weight:normal;padding:10px 18px;">마이리스트</a></li></ul></div></div>
                    # simple_join_btn = self.driver.find_element(By.CLASS_NAME, 'button_login2')
                    # simple_join_btn.click()

                    # self.simple_join()
                    break
            if endflag == True:
                break

            # //*[@id="contents_Wrap"]/div[5]/div/ul/li[2]/a
            # //*[@id="contents_Wrap"]/div[5]/div/ul/li[2]/a
            # //*[@id="contents_Wrap"]/div[5]/div/ul/li[2]/a
            #
            nextPageBtn = self.driver.find_element(By.XPATH, '//*[@id="contents_Wrap"]/div[5]/div/ul/li['+str(_page)+']/a')
            nextPageBtn.click()
            super().delay()

    def searchFakeKeywords(self, fkeywordCnt, fkeywordDelay):
        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=fkeywordCnt)

        for fKeyword in Keyword_3:
            try:
                print(fKeyword)
                # 책 제목 입력을 위한 검색창 클릭
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.ID, 'SearchWordBanner')
                search_box.click()

                search_box2 = self.driver.find_element(By.ID, 'SearchWord')
                search_box2.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                search_box2.click()

                search_box2.send_keys(fKeyword)

                super().delay()

                # 검색 버튼 클릭
                # document.getElementsByClassName('schBtn')[0].childNodes[0].click()
                btn = self.driver.find_element(By.CLASS_NAME, 'sch-go')
                btn.click()
                super().delay_n(fkeywordDelay)

                try:
                    addCartBtn = self.driver.find_element(By.XPATH,
                                                          '//*[@id="Search3_Result"]/div[4]/table/tbody/tr/td[3]/img')
                    addCartBtn.click()
                    super().delay_n(2)
                    addCartBtn = self.driver.find_element(By.XPATH, '//*[@id="Search3_Result"]/div[4]/div[2]/a[1]')
                    addCartBtn.click()
                except Exception as e:
                    print("do exception!! : ", e)
                    continue

            except Exception as e:
                logging.info("keyword loop exception!! : ", e)

        homebtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/h1')
        homebtn.click()
        super().delay_n(2)


    def closeAdPopup(self):
        try:
            # 오늘 그만보기
            pop_up_close_btn = self.driver.find_element(By.XPATH, '//*[@id="spaceEventLayer"]/div[1]/a[1]')
            pop_up_close_btn.click()
        except:
            a = 0

    def clickTargetBookInBest(self, keyword, delay_s):
        bestbtn = self.driver.find_element(By.XPATH,'//*[@id="welcom_wrap"]/div[9]/div/li[1]')
        bestbtn.click()
        super().delay()

        i = 0
        endflag = False
        for step in range(0,5):
            pageOffset = 0
            if step != 0:
                pageOffset = 2

            for _page in range(1, 6): # 7은 '>' 버튼, 8은 '>>' 버튼
                targets = self.driver.find_elements(By.CLASS_NAME, 'b_book_t')
                super().delay()
                for target in targets:
                    # step*250 + (page-1)*50
                    i = i + 1
                    if keyword in target.text:
                        # endflag = True
                        target.click()
                        self.rank = i
                        print('idx : ' + str(i))
                        logging.info('idx : ' + str(i))
                        logging.info(self.driver.current_url)
                        logging.info('clicked title : ' + self.driver.title)
                        print('clicked title : ' + self.driver.title)
                        addCartBtn = self.driver.find_element(By.ID, 'btnAddBasket')
                        addCartBtn.click()
                        self.doScrollDown(delay_s)
                        return self.rank
                if endflag == True:
                    break

                nextPageBtn = self.driver.find_element(By.XPATH, '//*[@id="contents_Wrap"]/div[5]/div/ul/li['+str((_page+1)+pageOffset)+']/a')
                nextPageBtn.click()
                super().delay()





    def clickSomething1(self):  # 알라딘이 만든 사은품
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

        Btn = self.driver.find_element(By.XPATH, '//*[@id="_ctl0_pGift"]/div/h2/a')
        ActionChains(self.driver).move_to_element(Btn).perform()
        Btn.click()
        self.delay_n(5)

        homeBtn = self.driver.find_element(By.XPATH, '//*[@id="fsHeader"]/h1/a')
        homeBtn.click()
    def clickChoiceOfMD(self):      # 편집장의 선택
        Btn = self.driver.find_element(By.XPATH, '//*[@id="welcom_wrap"]/div[11]/h2/a')
        ActionChains(self.driver).move_to_element(Btn).perform()

        Btn.click()
        self.delay_n(5)

        homeBtn = self.driver.find_element(By.XPATH, '/html/body/div[2]/h1')
        homeBtn.click()

    def aladin_best_phone_v2(self, keyword, page, n, title):
        fkeywordCnt = 2
        fkeywordDelay = 20
        targetDelay = 60
        super().printFuncInfo(self.aladin_best_phone_v2.__name__, keyword, page, n)

        self.closeAdPopup()

        self.aladin_login()

        self.clickChoiceOfMD()
        self.clickSomething1()

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        self.clickTargetBookInBest(title, targetDelay)


    def aladin_best_phone_v3(self, keyword, page, n, title):
        fkeywordCnt = 2
        fkeywordDelay = 20
        targetDelay = 60
        super().printFuncInfo(self.aladin_best_phone_v3.__name__, keyword, page, n)

        self.closeAdPopup()
        self.clickTargetBookInBest(title, targetDelay)
        # self.aladin_login()

        self.clickChoiceOfMD()
        self.clickSomething1()

        self.searchFakeKeywords(fkeywordCnt, fkeywordDelay)

        self.clickTargetBookInBest(title, targetDelay)
