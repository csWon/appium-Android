# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import Worker
from Tickets import ticketManager
import unittest

import yaml

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def tmp(suite):
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    # deviceInfo.yml에서 디바이스 정보 파싱
    with open('deviceInfo.yml') as f:
        deviceInfo = yaml.load(f, Loader=yaml.FullLoader)

    deviceInfoLength = len(deviceInfo['device'].items())

    port = 4721
    suiteArr = []

    tm = ticketManager()
    ticketList = tm.getTicket()
    idx = 0
    for k, v in deviceInfo['device'].items():
        suite = unittest.TestSuite()
        tickets = ticketList[idx]
        suite.addTest(Worker.worker('Do', v, '127.0.0.1:'+str(port), tickets))
        suiteArr.append(suite)
        port += 1
        idx += 1

    import multiprocessing

    with multiprocessing.Pool(processes=deviceInfoLength) as p:
        p.map(func=tmp, iterable=suiteArr)

