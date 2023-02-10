import time
import datetime
from Tickets import tickets
from DriverManager import driverManager

class worker():
    def Do(self):
        url_ip_check = 'https://ko.infobyip.com/'
        url_k_product = 'https://product.kyobobook.co.kr/'
        url_naver = 'https://www.naver.com'
        url_aladin = 'https://www.aladin.co.kr/'
        url_ypbook = 'https://www.ypbooks.co.kr/'

        _tickets = tickets()
        for ticket in _tickets.getTicket():
            # s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # logging.info('timeStamp : ' + s)
            for i in range(1, 500):
                start = time.time()
                dManager = driverManager()

                driver = dManager.open_browser_phone()

                try:
                    keyword = ticket[1]
                    page = ticket[2]
                    n = ticket[3]
                    title = ticket[4]

                    print('cycle : ' + str(i))

                    webPageClass = ticket[0](driver)
                    webPageClass.do(keyword, page, n, title)

                    # driver.quit()

                except Exception as e:
                    # print("exception!!! : ", traceback.format_exc())
                    print("error occured")
                    driver.quit()
                finally:
                    sec = time.time() - start
                    times = str(datetime.timedelta(seconds=sec)).split(".")
                    times = times[0]

                    print("총 걸린시간 : " + times)
                    print('------------------------------')