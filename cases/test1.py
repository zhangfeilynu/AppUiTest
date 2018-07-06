# /usr/bin/env python3

import os
import unittest
import time
import subprocess
from typing import Any, Union, List
from appium import webdriver
import logging.config
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# sys.path.append('D:\\PycharmProjects\\AppUiTest')
# import config.logging_config
# import config.read_config
from config import read_config
from config import logging_config
logging.config.dictConfig(logging_config.LOGGING)
logger = logging.getLogger('')


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



def getdevlist2():
    try:
        devlist = []
        logger.info('开始获取设备信息')
        device_info = subprocess.check_output('adb devices').decode().split('\r\n')
        for i in range(len(device_info)):
            if device_info[i].find('\tdevice') != -1:
                temp = device_info[i].split('\t')
                devlist.append(temp[0])
        logger.info('设备列表：{}'.format(devlist))
        if not devlist:
            logger.info('没有可用设备')
            sys.exit(1)
        return devlist
    except Exception as e:
        logger.error('获取设备失败：', e)
        sys.exit(1)


# 安装app
def install_app():
    try:
        apk_path = read_config.apk_path
        logger.info('安装APP')
        for i in range(len(device_list)):
            # cmd = 'adb  -s ' + device_list[i] + ' install ' + apk_path
            # assert isinstance(apk_path, str)
            cmd = ''.join(['adb  -s ', device_list[i], ' install ', apk_path])  # type: str
            result = subprocess.check_output(cmd)
            result = ''.join(result.decode().split())
            logger.info('{}安装结果:{}'.format(cmd, result))
    except subprocess.CalledProcessError as e:
        logger.error('安装app失败：', e)


# 启动app
def start_app():
    try:
        main_activity = read_config.main_activity
        logger.info('启动APP')
        for i in range(len(device_list)):
            # cmd = 'adb -s ' + device_list[i] + '  shell am start -n  ' + main_activity
            # assert isinstance(main_activity, str)
            cmd = ''.join(['adb -s ', device_list[i], '  shell am start -n  ', main_activity])  # type: str
            result = subprocess.check_output(cmd)
            result = ''.join(result.decode().split())
            logger.info('{}启动结果:{}'.format(cmd,  result))
    except subprocess.CalledProcessError as e:
        logger.error('启动app失败：', e)


# 卸载app
def uninstall_app():
    try:
        package_name = read_config.package_name
        logger.info('卸载APP')
        for i in range(len(device_list)):
            # cmd = 'adb -s ' + device_list[i] + ' uninstall ' + package_name
            # assert isinstance(package_name, str)
            cmd = ''.join(['adb -s ', device_list[i], ' uninstall ', package_name])  # type: str
            result = subprocess.check_output(cmd)
            result = ''.join(result.decode().split())
            logger.info('{}卸载结果:{}'.format(cmd,  result))
    except subprocess.CalledProcessError as e:
        logger.error('卸载app失败：', e)


if __name__ == '__main__':
    device_list = []
    device_list = getdevlist2()
    install_app()
    time.sleep(5)
    start_app()
    time.sleep(5)
    uninstall_app()
