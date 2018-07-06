#/usr/bin/env python3


# import os,subprocess
# import re
#
# def connect_device():
#     '''检查设备是否连接成功，如果成功返回True，否则返回False'''
#     try:
#         '''获取设备列表信息，并用\r\n拆分'''
#         device_info = subprocess.check_output('adb devices').split('\r\n'.encode(encoding='utf-8'))
#         '''如果没有链接设备或者设备读取失败，第二个元素为空'''
#         if device_info[1] == '':
#             return False
#         else:
#             return True
#     except Exception as e:
#         print('Device Connect Fail:', e)
#
# def get_android_version():
#     try:
#         if connect_device():
#             # 获取系统设备系统信息
#             sys_info = subprocess.check_output('adb shell cat /system/build.prop')
#             # 获取安卓版本号
#             android_version = re.findall('version.release=(\d\.\d)*'.encode(encoding='utf-8'), sys_info, re.S)[0]
#             return android_version
#         else:
#             return 'Connect Fail,Please reconnect Device...'
#     except Exception as e:
#         print('Get Android Version:',e)
#
# def get_device_name():
#     try:
#         if connect_device():
#             #获取设备名
#             device_info = subprocess.check_output('adb devices -l')
#             device_name = re.findall(r'device product:(.*)\smodel'.encode(encoding='utf-8'),device_info,re.S)[0]
#             return device_name
#         else:
#             return 'Connect Fail,Please reconnect Device...'
#     except Exception as e:
#         print('Get Device Name:',e)
# print(get_device_name(),get_android_version())
# print(get_android_version())


import os

# 获取username, 如chinaren
def getusername():
    '''
    利用echo %username%打印出username,然后去掉输出中无用的字符
    '''
    namelist = os.popen('echo %username%').readlines()
    username = namelist[0].replace("\n", "")
    # 获取当前的username
    return username






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





print(getusername())
print(getdevlist())



