
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import inspect, os, platform, time, random, sys
# import chromedriver_autoinstaller

class driverManager:
    # 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36',
    # 'Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.52 Mobile/15E148 Safari/604.1',
    # 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.52 Mobile/15E148 Safari/604.1',
    # 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1',
    # 'Mozilla/5.0 (iPad; CPU OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1',
    # 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/107.0 Mobile/15E148 Safari/605.1.15',
    # 'Mozilla/5.0 (iPad; CPU OS 13_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/107.0 Mobile/15E148 Safari/605.1.15',
    # 'Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/107.0',
    # 'Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:107.0) Gecko/107.0 Firefox/107.0',
    # 'Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62',
    # 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62',
    # 'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62',
    # 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.79 Mobile Safari/537.36 EdgA/107.0.1418.62'

    def get_ua(self):
        ua_list = [
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
                    'Mozilla/5.0 (X11; Linux i686; rv:107.0) Gecko/20100101 Firefox/107.0',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Mozilla/5.0 (X11; Linux i686; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/107.0.1418.68',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/107.0.1418.68',
                    ]
        ua = random.choice(ua_list)
        print(ua)
        return ua

    def open_browser_phone(self):
        import datetime
        import time
        from selenium.webdriver.common.by import By

        dc = {
            "platformName": "Android",
            "platformVersion": "9.0",
            "deviceName": "ce10171ab8ac5f3e04",
            #"deviceName": "ce05171555816f1b03",
            "browserName": "chrome",
            "browserVersion":"109.0.5414.86"
            # "browserVersion": "109.0.5414.117"
        }

        # dc = {}
        # dc["platformName"] = "Android"
        # dc["platformVersion"] = "9.0"
        # dc["deviceName"] = "ce05171555816f1b03"
        # dc["browserName"] = "chrome"
        # dc["browserVersion"] = "109.0.5414.86"

        # chrome_options = webdriver.ChromeOptions()
        # # 옵션 설정
        # chrome_options.add_argument("platformName:Android")
        # chrome_options.add_argument("platformVersion:9.0")
        # chrome_options.add_argument("deviceName:ce10171ab8ac5f3e04")
        # chrome_options.add_argument("browserName:chrome")
        # chrome_options.add_argument("browserVersion:109.0.5414.117")
        # user_agent = self.get_ua()
        # chrome_options.add_argument('user-agent=' + user_agent)

        # 브라우저 열기
        # self.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe', options=chrome_options)
        # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)
        # driver.get('https://www.aladin.co.kr/')
        start = time.time()

        # self.driver.implicitly_wait(10)
        # self.driver.get('https://whatismyipaddress.com/')

        self.driver.execute_script('mobile: shell', {
        'command': 'svc',
        'args': ['data', 'disable'],
        'timeout': 5000
        })

        self.driver.execute_script('mobile: shell', {
        'command': 'svc',
        'args': ['data', 'enable'],
        'timeout': 5000
        })

        while True:
            try:
                self.driver.implicitly_wait(60)
                self.driver.get('http://20.196.196.177/index2.html')
                time.sleep(5)
            except:
                self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)
                print("ERROR: Waiting for connection with appium server !!!")
                time.sleep(1)
            else:
                break


        # adb shell svc data disable
        # adb shell settings put global airplane_mode_on 1
        #
        # adb shell svc data enable
        # adb shell settings put global airplane_mode_on 0

        # dom 내려온 다음 실행하게 하는 함수

        sec = time.time() - start
        times = str(datetime.timedelta(seconds=sec)).split(".")
        times = times[0]

        print("connecting time " + times)

        return self.driver

    def open_browser_Proxy(self):
        # chrome_path = '/usr/local/bin/chromedriver'
        # torexe = os.popen(r'/usr/local/bin/tor')
        # torexe = os.popen(r'/opt/homebrew/opt/tor/bin/tor')
        # PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
        # PROXY = "socks5://127.0.0.1:9150"  # IP:PORT or HOST:PORT
        # chromedriver_autoinstaller.install()

        prx = open('ip.txt', 'r').read().split('\n')

        # 프록시 랜덤 선택
        PROXY = random.choice(prx)
        print("proxy : " + PROXY)

        chrome_options = webdriver.ChromeOptions()
        # options.add_argument('window-size=1920,1080')
        # 옵션 설정
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("disable-infobars")
        # chrome_options.page_load_strategy = 'normal'
        # chrome_options.add_argument('--enable-automation')
        # chrome_options.add_argument('disable-infobars')
        # chrome_options.add_argument('disable-gpu')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('user-agent={}'.format(useragent)) # todo 설정 필요
        # chrome_options.add_argument('--lang=ko_KR')
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--allow-insecure-localhost')
        # chrome_options.add_argument('--allow-running-insecure-content')
        # chrome_options.add_argument('--disable-notifications')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-browser-side-navigation')
        # chrome_options.add_argument('--mute-audio')
        # #    # Tor 프록시 설정 (ip 우회)
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        # chrome_options.headless = True
        user_agent = self.get_ua()
        chrome_options.add_argument('user-agent=' + user_agent)

        # 아이피 적용
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "proxyType": "MANUAL"
        }

        # 브라우저 열기
        # self.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe', options=chrome_options)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)
        print('------------------------------')

        return self.driver