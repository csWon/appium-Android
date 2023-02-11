import requests
import json
import traceback

class loggingManager:
    url = 'http://20.196.196.177:8081/dnc/log/addLog.do'
    def logging(self, site, ticketNm, deviceId, status, rank, loadTime, errorMsg):
        data = {
            "site": site,
            "ticketNm": ticketNm,
            "deviceId": deviceId,
            "status": status,
            "rank": rank,
            "loadTime": loadTime,
            "errorMsg": errorMsg
        }
        response = self.web_request(method_name='POST', url=self.url, dict_data=data, is_urlencoded=True);
        print(response);


    def web_request(self, method_name, url, dict_data, is_urlencoded=True):
        _method_name = method_name.upper()
        if _method_name not in ('GET', 'POST'):
            raise Exception('method_name is GET or POST plz...')

        try :
            if _method_name == 'GET':
                response = requests.get(url=url, params=dict_data)
            elif _method_name == 'POST':
                if is_urlencoded is True:
                    response = requests.post(url=url, data=dict_data,
                                             headers={'Content-Type': 'application/x-www-form-urlencoded'})
                else:
                    response = requests.post(url=url, data=json.dumps(dict_data),
                                             headers={'Content-Type': 'application/json'})
            print(response)
        except Exception as e:
            print(traceback.format_exception_only(e));

