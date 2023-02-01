from BookStore import bookStore
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string

class aladin(bookStore):
    def __init__(self, driver):
        # bookStore.__init__(self)
        self.driver = driver

    def do(self, keyword, page, n, title):
        self.aladin_best_phone_v1(keyword, page, n, title)

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


    def aladin_best_phone_v1(self, keyword, page, n, title):
        super().printFuncInfo(self.aladin_best_phone_v1.__name__, keyword, page, n)
        page = page - 2
        n = n - 1

        self.driver.get(super().url_aladin)
        cookies = self.driver.get_cookies()
        self.driver.delete_all_cookies()
        cookies = self.driver.get_cookies()

        #'//*[@id="spaceEventLayer"]/div[1]/a[2]
        pop_up_close_btn = self.driver.find_element(By.XPATH, '//*[@id="spaceEventLayer"]/div[1]/a[2]')
        pop_up_close_btn.click()

        # simple_join_btn = self.driver.find_element(By.CLASS_NAME, 'set3m')
        # simple_join_btn.click()

        # self.simple_join()

        fakeKeywords = open('keyword.txt', 'r', encoding='UTF8').read().split('\n')
        Keyword_3 = random.choices(fakeKeywords, k=2)
        Keyword_3.append(title)
        for fKeyword in Keyword_3:
            try:
                # 책 제목 입력
                # document.getElementsByClassName('iptTxt')[0].value = '영어회화'
                search_box = self.driver.find_element(By.ID, 'SearchWordBanner')

                # search_box.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
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

                addCartBtn = self.driver.find_element(By.XPATH, '//*[@id="Search3_Result"]/div[4]/table/tbody/tr/td[3]/img')
                addCartBtn.click()
                super().delay_n(2)

                addCartBtn = self.driver.find_element(By.XPATH, '//*[@id="Search3_Result"]/div[4]/div[2]/a[1]')
                addCartBtn.click()


            except Exception as e:
                logging.info("loop exception!! : ", e)

        homebtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/h1')
        homebtn.click()
        super().delay_n(2)

        pop_up_close_btn = self.driver.find_element(By.XPATH, '//*[@id="spaceEventLayer"]/div[1]/a[2]')
        pop_up_close_btn.click()

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
                    logging.info('idx : ' + str(i))
                    logging.info(self.driver.current_url)
                    logging.info('clicked title : ' + self.driver.title)
                    print('clicked title : ' + self.driver.title)
                    addCartBtn = self.driver.find_element(By.ID, 'btnAddBasket')
                    addCartBtn.click()
                    super().delay()

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

        super().delay_n(10)