#/usr/bin/env python3


import os
import unittest
import time
import shlex
import subprocess
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

def getdevlist2():
    try:
        devlist = []
        device_info = subprocess.check_output('adb devices').decode().split('\r\n')
        for i in range(len(device_info)):
            if device_info[i].find('\tdevice') != -1:
                temp = device_info[i].split('\t')
                devlist.append(temp[0])
        # for i in range(len(devlist)):
        #     devlist[i].decode()  #转码
        return devlist
        # print(devlist)
        # print(device_info)
        # if device_info[1] == '':
        #     return False
        # else:
        #     return True
    except Exception as e:
        print('Device Connect Fail:',e)



#安装app
def install_app():
    for i in range(len(device_list)):
        # str = 'adb  -s ' + device_list[i] + ' install D:\\workspace\\hmautotest\\apps\\c_main.apk'
        # result = subprocess.check_output(str)
        # print('安装结果：', result)
        cmd = 'adb  -s ' + device_list[i] + ' install D:\\workspace\\hmautotest\\apps\\c_main.apk'
        # cmd = shlex.split(shell_cmd)
        # p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p = subprocess.Popen(cmd)
        p.wait()
        print('执行结果：', p.returncode)



#启动app
def start_app():
    for i in range(len(device_list)):
        # str = 'adb -s ' + device_list[i] + '  shell am start -n  com.redstar.mainapp/.business.LaunchActivity'
        # result = subprocess.check_output(str)
        # print('启动结果：', result)
        cmd = 'adb  -s ' + device_list[i] + ' shell am start -n  com.redstar.mainapp/.business.LaunchActivity'
        # cmd = shlex.split(shell_cmd)
        # p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p = subprocess.Popen(cmd)
        p.wait()
        print('执行结果：', p.returncode)


#卸载app
def uninstall_app():
    for i in range(len(device_list)):
        # str = 'adb -s ' + device_list[i] + ' uninstall com.redstar.mainapp'
        # result = subprocess.check_output(str)
        # print('卸载结果：', result)
        cmd = 'adb  -s ' + device_list[i] + ' uninstall com.redstar.mainapp'
        # cmd = shlex.split(shell_cmd)
        # p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p = subprocess.Popen(cmd)
        p.wait()
        print('执行结果：', p.returncode)





if __name__ == '__main__':
    device_list = []
    device_list = getdevlist2()
    print(device_list)
    install_app()
    time.sleep(5)
    start_app()
    time.sleep(5)
    uninstall_app()



# print(getdevlist2())






