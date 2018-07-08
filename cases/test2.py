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


'''
从test1.py复制过来；
根据result存储各个步骤的操作结果
summary
execUid//执行编号（区分每次测试执行）
devicesList//设备列表
resultStatus//测试结果
startTime//开始时间
endTime//结束时间
createDate//创建时间
duration//耗时

details  数组
execUid//执行编号
deviceName//设备名称
stepId//步骤编号，1安装2启动3卸载
resultStatus//执行结果0成功1失败
resultContent//命令返回内容
startTime//开始时间
endTime//结束时间
duration//耗时
'''
devlist = []  #设备列表
dellist = [] #需要删除的设备列表
summary = {} #汇总报告
details = [] #每个设备每步的详细报告列表
detail = {} #单个设备某一步骤的报告
report = {summary, details} #单次执行的测试报告
# 找设备
def getdevlist():
    try:
        # devlist = []
        logger.info('开始获取设备信息')
        device_info = subprocess.check_output('adb devices').decode().split('\r\n')
        for i in range(len(device_info)):
            if device_info[i].find('\tdevice') != -1:
                temp = device_info[i].split('\t')
                devlist.append(temp[0])
        logger.info('设备列表：{}'.format(devlist))
        if not devlist:
            logger.info('没有可用设备')
            # return
            sys.exit(0)
        return devlist
    except Exception as e:
        logger.error('获取设备失败：', e)
        sys.exit(0)


# 安装app
def install_app():
    try:
        apk_path = read_config.apk_path
        logger.info('安装APP')
        for i in range(len(devlist)):
            # cmd = 'adb  -s ' + device_list[i] + ' install ' + apk_path
            # assert isinstance(apk_path, str)
            cmd = ''.join(['adb  -s ', devlist[i], ' install ', apk_path])  # type: str
            result = subprocess.check_output(cmd)
            result = ''.join(result.decode().split())
            logger.info('{}安装结果:{}'.format(cmd, result))
            if not result.__contains__('Success'):
                # del devlist[i]
                dellist.append(devlist[i])
        for i in range(len(dellist)):#删除执行失败的设备，下一步不执行操作
            devlist.remove(dellist[i])
        if not devlist:
            sys.exit(0)
    except subprocess.CalledProcessError as e:
        logger.error('安装app失败：', e)
        sys.exit(1)


# 启动app
def start_app():
    try:
        main_activity = read_config.main_activity
        logger.info('启动APP')
        for i in range(len(devlist)):
            # cmd = 'adb -s ' + device_list[i] + '  shell am start -n  ' + main_activity
            # assert isinstance(main_activity, str)
            cmd = ''.join(['adb -s ', devlist[i], '  shell am start -n  ', main_activity])  # type: str
            result = subprocess.check_output(cmd)
            result = ''.join(result.decode().split())
            logger.info('{}启动结果:{}'.format(cmd,  result))
    except subprocess.CalledProcessError as e:
        logger.error('启动app失败：', e)
        sys.exit(1)


# 卸载app
def uninstall_app():
    try:
        package_name = read_config.package_name
        logger.info('卸载APP')
        for i in range(len(devlist)):
            # cmd = 'adb -s ' + device_list[i] + ' uninstall ' + package_name
            # assert isinstance(package_name, str)
            cmd = ''.join(['adb -s ', devlist[i], ' uninstall ', package_name])  # type: str
            result = subprocess.check_output(cmd)
            result = ''.join(result.decode().split())
            logger.info('{}卸载结果:{}'.format(cmd,  result))
    except subprocess.CalledProcessError as e:
        logger.error('卸载app失败：', e)
        sys.exit(1)


if __name__ == '__main__':
    # device_list = []
    # device_list = getdevlist()
    getdevlist()
    install_app()
    time.sleep(5)
    start_app()
    time.sleep(5)
    uninstall_app()
