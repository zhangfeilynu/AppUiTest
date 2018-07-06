#/usr/bin/env python3

import os
import unittest
import time
from appium import webdriver
PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '335769430804'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] ='True'
desired_caps['app'] = PATH('D:\\workspace\\hmautotest\\apps\\c_main.apk')
desired_caps['appPackage'] = 'com.redstar.mainapp'
desired_caps['appActivity'] = 'com.redstar.mainapp.business.LaunchActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(20)
driver.find_element_by_link_text('我的').click()
time.sleep(5)
driver.quit()
