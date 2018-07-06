#/usr/bin/env python3


import os,subprocess
import re

def connect_device():
    '''检查设备是否连接成功，如果成功返回True，否则返回False'''
    '''获取设备列表信息，并用\r\n拆分'''
    device_info = subprocess.check_output('adb devices').split('\r\n')
    '''如果没有链接设备或者设备读取失败，第二个元素为空'''
    if device_info[1] == '':
         return False
    else:
         return True


def get_android_version():
    if connect_device():
        # 获取系统设备系统信息
        sys_info = subprocess.check_output('adb shell cat /system/build.prop')
        # 获取安卓版本号
        android_version = re.findall('version.release=(\d\.\d)*',sys_info,re.S)[0]
        return android_version
    else:
            return 'Connect Fail,Please reconnect Device...'


def get_device_name():
    try:
        if connect_device():
            #获取设备名
            device_info = subprocess.check_output('adb devices -l')
            device_name = re.findall(r'device product:(.*)\smodel',device_info,re.S)[0]
            return device_name
        else:
            return 'Connect Fail,Please reconnect Device...'
    except Exception as e:
        print('Get Device Name:',e)


print(get_device_name())
print(get_android_version())



