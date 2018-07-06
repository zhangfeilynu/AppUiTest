#coding=utf-8

import os
# import sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if not os.path.isdir(BASE_DIR):
#     os.mkdir(BASE_DIR)

# 日志相关配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s : %(message)s'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d : %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        }
    },

    'handlers': {
         'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
         },

         'debug': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join('../logs/', 'debug.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'standard',
         },
         'info': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join('../logs/', 'info.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
         },
         'warn': {
             'level': 'WARNING',
             'class':'logging.handlers.RotatingFileHandler',
             'formatter': 'simple',
             'filename':os.path.join('../logs/', 'warn.log'),
             'maxBytes': 1024*1024*5, # 5 MB
             'backupCount': 5,
             'mode': 'a',
         },
         'error': {
             'level': 'ERROR',
             'class':'logging.handlers.RotatingFileHandler',
             'formatter': 'simple',
             'filename':os.path.join('../logs/', 'error.log'),
             'maxBytes': 1024*1024*5, # 5 MB
             'backupCount': 5,
             'mode': 'a',
         },
    },

    'loggers': {
        '': {
            'handlers': ['console', 'debug', 'info', 'warn', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
    },
}