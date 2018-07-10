# /usr/bin/env python3

import os
import unittest
import time
from datetime import datetime
import subprocess
import json
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
from common import utils
from dateutil import parser
logging.config.dictConfig(logging_config.LOGGING)
logger = logging.getLogger('')


'''
从test2.py复制过来；
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
exec_uid = utils.generate_random()
details = [] #每个设备每步的详细报告列表
# detail = {} #单个设备某一步骤的报告
# report = {summary, details} #单次执行的测试报告
report = {}
# 找设备
def getdevlist():
    try:
        # devlist = []
        # exec_uid = str(datetime.now())
        summary.setdefault('exec_uid', exec_uid)  #测试唯一编号
        summary.setdefault('start_time', int(round(time.time() * 1000)))  #.总体测试开始时间，精确到ms
        logger.info('开始获取设备信息')
        device_info = subprocess.check_output('adb devices').decode().split('\r\n')
        for i in range(len(device_info)):
            if device_info[i].find('\tdevice') != -1:
                temp = device_info[i].split('\t')
                devlist.append(temp[0])
        logger.info('设备列表：{}'.format(devlist))
        # summary.setdefault('devices_list', devlist)
        _devlist = devlist[::]
        summary['devices_list'] = _devlist
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
        # apk_path = read_config.apk_path
        apk_path = ''.join([rootPath, '\\apps\\', read_config.apk_path])
        logger.info('安装APP')
        for i in range(len(devlist)):
            # cmd = 'adb  -s ' + device_list[i] + ' install ' + apk_path
            # assert isinstance(apk_path, str)
            detail = {}
            detail.setdefault('exec_uid', exec_uid) #测试编号
            detail.setdefault('device_name', devlist[i])
            detail.setdefault('step_id', 0) #0对应安装APP
            detail.setdefault('start_time', int(round(time.time() * 1000)))
            cmd = ''.join(['adb  -s ', devlist[i], ' install ', apk_path])  # type: str
            result = subprocess.check_output(cmd)
            detail.setdefault('end_time', int(round(time.time() * 1000)))
            detail.setdefault('duration', detail.get('end_time') - detail.get('start_time'))

            start_time = time.localtime(detail.get('start_time') / 1000)
            detail['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S", start_time)  # 格式化开始时间
            end_time = time.localtime(detail.get('end_time') / 1000)
            detail['end_time'] = time.strftime("%Y-%m-%d %H:%M:%S", end_time)  # 格式化结束时间

            result = ''.join(result.decode().split())
            detail.setdefault('result_status', 'pass')
            detail.setdefault('result_content', result)
            logger.info('{}安装结果:{}'.format(cmd, result))
            if not result.__contains__('Success'):
                # del devlist[i]
                detail['result_status'] = 'fail'  #否则该步骤重置为失败
                dellist.append(devlist[i])
            details.append(detail)
        for i in range(len(dellist)):#删除执行失败的设备，下一步不执行操作
            devlist.remove(dellist[i])
        if not devlist:
            summary.setdefault('details', details)
            summary.setdefault('end_time', int(round(time.time() * 1000)))  # 总体测试结束时间，精确到ms
            summary.setdefault('duration', summary.get('end_time') - summary.get('start_time'))
            start_time = time.localtime(summary.get('start_time') / 1000)
            summary['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S", start_time)  # 格式化开始时间
            end_time = time.localtime(summary.get('end_time') / 1000)
            summary['end_time'] = time.strftime("%Y-%m-%d %H:%M:%S", end_time)  # 格式化结束时间
            summary.setdefault('result_status', 'fail')
            # 存储测试结果
            file_name = ''.join([rootPath, '/testoutput/', exec_uid, '.json'])
            f = open(file_name, 'w')
            f.write(str(summary))
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
            detail = {}
            detail.setdefault('exec_uid', exec_uid)  # 测试编号
            detail.setdefault('device_name', devlist[i])
            detail.setdefault('step_id', 1)  # 1对应启动APP
            detail.setdefault('start_time', int(round(time.time() * 1000)))
            cmd = ''.join(['adb -s ', devlist[i], '  shell am start -n  ', main_activity])  # type: str
            result = subprocess.check_output(cmd)

            detail.setdefault('end_time', int(round(time.time() * 1000)))
            detail.setdefault('duration', detail.get('end_time') - detail.get('start_time'))

            start_time = time.localtime(detail.get('start_time') / 1000)
            detail['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S", start_time)  # 格式化开始时间
            end_time = time.localtime(detail.get('end_time') / 1000)
            detail['end_time'] = time.strftime("%Y-%m-%d %H:%M:%S", end_time)  # 格式化结束时间
            result = ''.join(result.decode().split())
            detail.setdefault('result_status', 'pass')
            detail.setdefault('result_content', result)

            logger.info('{}启动结果:{}'.format(cmd,  result))

            if result != read_config.start_result:
                detail['result_status'] = 'fail'  # 否则该步骤重置为失败
            details.append(detail)
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
            detail = {}
            detail.setdefault('exec_uid', exec_uid)  # 测试编号
            detail.setdefault('device_name', devlist[i])
            detail.setdefault('step_id', 2)  # 2对应卸载APP
            detail.setdefault('start_time', int(round(time.time() * 1000)))
            cmd = ''.join(['adb -s ', devlist[i], ' uninstall ', package_name])  # type: str
            result = subprocess.check_output(cmd)
            detail.setdefault('end_time', int(round(time.time() * 1000)))
            detail.setdefault('duration', detail.get('end_time') - detail.get('start_time'))

            start_time = time.localtime(detail.get('start_time') / 1000)
            detail['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S", start_time)  # 格式化开始时间
            end_time = time.localtime(detail.get('end_time') / 1000)
            detail['end_time'] = time.strftime("%Y-%m-%d %H:%M:%S", end_time)  # 格式化结束时间

            result = ''.join(result.decode().split())

            detail.setdefault('result_status', 'pass')
            detail.setdefault('result_content', result)

            logger.info('{}卸载结果:{}'.format(cmd,  result))

            if not result.__contains__('Success'):
                # del devlist[i]
                detail['result_status'] = 'fail'  #否则该步骤重置为失败
            details.append(detail)
        summary.setdefault('details', details)
        summary.setdefault('end_time', int(round(time.time() * 1000)))  # 总体测试结束时间，精确到ms
        summary.setdefault('duration', summary.get('end_time') - summary.get('start_time'))
        start_time = time.localtime(summary.get('start_time') / 1000)
        summary['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S", start_time)  # 格式化开始时间
        end_time = time.localtime(summary.get('end_time') / 1000)
        summary['end_time'] = time.strftime("%Y-%m-%d %H:%M:%S", end_time)  # 格式化结束时间
        summary.setdefault('result_status', 'pass')
        for i in range(len(details)):
            if details[i].get('result_status') == 'fail':
                summary['result_status'] = 'fail'  #如果存在失败的步骤，则整个测试失败
                break

        #存储测试结果
        file_name = ''.join([rootPath, '/testoutput/', exec_uid, '.json'])
        f = open(file_name, 'w')
        f.write(str(summary))
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
    # print(summary)

