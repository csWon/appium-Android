import time
import datetime
from Tickets import ticketManager
from DriverManager import driverManager
import unittest
from LoggingManager import loggingManager
import traceback

class worker(unittest.TestCase):
    def __init__(self, method_name, dc, server_ip, tickets):
        super(worker, self).__init__(method_name)
        self.dc = dc
        self.server_ip = server_ip
        self.dManager = driverManager(self.dc, self.server_ip)
        self.driver = ''
        self.tickets = tickets

    def setUp(self):
        self.do_nothing = 0
    def tearDown(self):
        if self.driver != '':
            self.driver.quit()

    def Do(self):
        url_ip_check = 'https://ko.infobyip.com/'
        url_k_product = 'https://www.kyobobook.co.kr/'
        url_naver = 'https://www.naver.com'
        url_aladin = 'https://www.aladin.co.kr/'
        url_ypbook = 'https://www.ypbooks.co.kr/'

        for i in range(1, 60):
            # s = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # logging.info('timeStamp : ' + s)
            for ticket in self.tickets:
                start = time.time()

                logger = loggingManager()
                self.driver = self.dManager.open_browser_phone()

                status = 'S'
                errorMsg = ''
                try:
                    keyword = ticket[1]
                    page = ticket[2]
                    n = ticket[3]
                    title = ticket[4]
                    doIdx = ticket[5]

                    print('cycle : ' + str(i))

                    publisherClass = ticket[0](self.driver)

                    dic = publisherClass.do(keyword, page, n, title, doIdx)
                    rank = dic['rank']
                    func = dic['func']
                    id = dic['id']
                    pw = dic['pw']
                    self.driver.quit()

                except Exception as e:
                    print(self.dManager.dc.get("deviceName"), "exception!!! : ", traceback.format_exc())
                    print("error occured")
                    self.driver.quit()
                    status = 'F'
                    rank = 0
                    func = ''
                    id = ''
                    pw = ''
                    errorMsg = traceback.format_exception_only(type(e), e)

                finally:
                    sec = time.time() - start
                    print(sec)
                    times = str(datetime.timedelta(seconds=sec)).split(".")
                    times = times[0]

                    print("총 걸린시간 : " + times)

                    logger.logging(site=ticket[0].__name__,
                                   ticketNm=ticket[4].replace(" ", "_"),
                                   deviceId=self.dManager.dc.get("deviceName"),
                                   id=id,
                                   pw=pw,
                                   func=func,
                                   status=status,
                                   rank=rank,
                                   loadTime=sec,
                                   ip=self.dManager.client_ip,
                                   errorMsg=errorMsg);
                    print('------------------------------')