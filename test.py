#/usr/bin/env python3


import os
import unittest
import time
from appium import webdriver
# 获取设备SN列表
def getdevlist():
    '''
    利用adb devices先输出所有已连接上的android devices,然后去掉输出中无用的字符,只保留devices SN
    '''
    devlist = []
    connectfile = os.popen('adb devices')
    list = connectfile.readlines()
    # print(list)
    for i in range(len(list)):
        if list[i].find('\tdevice') != -1:
            temp = list[i].split('\t')
            devlist.append(temp[0])
    return devlist

# PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

# desired_caps = {}
# # desired_caps['platformName'] = 'Android'
# # desired_caps['platformVersion'] = '6.0.1'
# # desired_caps['deviceName'] = getdevlist()
# # desired_caps['unicodeKeyboard'] = 'True'
# # desired_caps['resetKeyboard'] ='True'
# # desired_caps['app'] = PATH('D:\\workspace\\hmautotest\\apps\\c_main.apk')
# # desired_caps['appPackage'] = 'com.redstar.mainapp'
# # desired_caps['appActivity'] = 'com.redstar.mainapp.business.LaunchActivity'
# # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# # time.sleep(20)
# # # driver.find_element_by_link_text('我的').click()
# # # time.sleep(5)
# # driver.quit()
# print(getdevlist())

device_list = []
device_list = getdevlist()

#安装app
def install_app():
    for i in range(len(device_list)):
        str = 'adb  -s ' + device_list[i] + ' install D:\\workspace\\hmautotest\\apps\\c_main.apk'
        result = os.popen(str)
        print('安装结果：', result.read()) # 需要获取返回结果...
        # print(str)



#启动app
def start_app():
    for i in range(len(device_list)):
        str = 'adb -s ' + device_list[i] + '  shell am start -n  com.redstar.mainapp/.business.LaunchActivity'
        result = os.popen(str)
        print('启动结果：', result.read())  # 需要获取返回结果...
        # print(str)


#卸载app
def uninstall_app():
    for i in range(len(device_list)):
        str = 'adb -s ' + device_list[i] + ' uninstall com.redstar.mainapp'
        result = os.popen(str)
        print('卸载结果：', result.read()) # 需要获取返回结果...
        # print(str)




install_app()
time.sleep(5)
start_app()
time.sleep(5)
uninstall_app()








