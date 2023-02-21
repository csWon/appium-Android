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

    dc1 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce0317136d6b60b10c",
        "udid": "ce0317136d6b60b10c",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.117"
    }

    dc2 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce05171555816f1b03",
        "udid": "ce05171555816f1b03",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.86"
    }

    dc3 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce051715544da4e30d",
        "udid": "ce051715544da4e30d",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.117"
    }

    dc4 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce0817180bec302b0c",
        "udid": "ce0817180bec302b0c",
        "browserName": "chrome",
        "browserVersion": "110.0.5481.65"
    }

    dc5 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce0517155912102e01",
        "udid": "ce0517155912102e01",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.117"
    }

    dc6 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce061716d834ec260d",
        "udid": "ce061716d834ec260d",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.117"
    }

    dc7 = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "ce091719ead6de2902",
        "udid": "ce091719ead6de2902",
        "browserName": "chrome",
        "browserVersion": "109.0.5414.117"
    }


    # 110.0.5481
    suite1 = unittest.TestSuite()
    suite1.addTest(Worker.worker('Do', dc1, '127.0.0.1:4723'))

    suite2 = unittest.TestSuite()
    suite2.addTest(Worker.worker('Do', dc2, '127.0.0.1:4724'))

    suite3 = unittest.TestSuite()
    suite3.addTest(Worker.worker('Do', dc3, '127.0.0.1:4725'))

    suite4 = unittest.TestSuite()
    suite4.addTest(Worker.worker('Do', dc4, '127.0.0.1:4726'))

    suite5 = unittest.TestSuite()
    suite5.addTest(Worker.worker('Do', dc5, '127.0.0.1:4727'))

    suite6 = unittest.TestSuite()
    suite6.addTest(Worker.worker('Do', dc6, '127.0.0.1:4728'))

    suite7 = unittest.TestSuite()
    suite7.addTest(Worker.worker('Do', dc7, '127.0.0.1:4729'))

    # suite_test = unittest.TestSuite()
    # suite_test.addTest(Worker.worker('Do', dc4_test, '127.0.0.1:4730'))


    import multiprocessing

    with multiprocessing.Pool(processes=6) as p:
        p.map(func=tmp, iterable=[ suite1, suite2, suite3, suite4, suite5, suite6])
        # p.map(func=tmp, iterable=[suite6])

    #
    # import multiprocessing
    #
    # with multiprocessing.Pool(processes=2) as p:
    #     p.map(func=tmp, iterable=[suite2, suite1])
    #
    # th1 = Process(target=work, args=(dc,"127.0.0.1:4723"))
    # th2 = Process(target=work, args=(dc2, "127.0.0.1:4724"))
    #
    # th1.start()
    # th2.start()
    #
    # th1.join()
    # th2.join()


