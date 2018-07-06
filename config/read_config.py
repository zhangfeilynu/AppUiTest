#coding=utf-8

import os
import configparser
# import sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
#获取文件的当前路径（绝对路径）
cur_path = os.path.dirname(os.path.realpath(__file__))

#获取config.ini的路径
config_path = os.path.join(cur_path, 'config.ini')

conf = configparser.ConfigParser()
conf.read(config_path)

apk_path = conf.get('app', 'apk_path')
main_activity = conf.get('app', 'main_activity')
package_name = conf.get('app', 'package_name')


# print(rootPath)