# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from appium import webdriver
# from BookStore import bookStore
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string
import time

import Worker
import datetime
import logging
from Tickets import tickets
from DriverManager import driverManager
from LoggingManager import loggingManager

import traceback
from multiprocessing import Process, Queue

import unittest

import yaml

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



def tmp(suite):
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    # ce0317136d6b60b10c
    # ce05171555816f1b03
    # ce0517155912102e01
    # ce051715544da4e30d
    # ce0817180bec302b0c

    # deviceInfo.yml에서 디바이스 정보 파싱
    with open('deviceInfo.yml') as f:
        deviceInfo = yaml.load(f, Loader=yaml.FullLoader)

    deviceInfoLength = len(deviceInfo['device'].items())

    port = 4721
    suiteArr = []

    for k, v in deviceInfo['device'].items():
        suite = unittest.TestSuite()
        suite.addTest(Worker.worker('Do', v, '127.0.0.1:'+str(port)))
        suiteArr.append(suite)
        port += 1

    import multiprocessing

    with multiprocessing.Pool(processes=deviceInfoLength) as p:
        p.map(func=tmp, iterable=suiteArr)

