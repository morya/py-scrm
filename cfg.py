#coding:utf8

#coding:utf-8

import logging.config


def cfgLogging():
    LOGGING = {
               'version': 1,
               'disable_existing_loggers': True,
               'formatters': {
                              'default': {'format': '[%(asctime)-25s] [%(relativeCreated)-15s] %(name)-12s pid:%(process)d %(message)s'},
                               # default': {
                               #           'format' : '%(asctime)s %(message)s',
                               #           'datefmt' : '%Y-%m-%d %H:%M:%S'
                               # }
                },
               'handlers': {
                            'console':{
                                       'level':'DEBUG',
                                       'class':'logging.StreamHandler',
                                       'formatter': 'default'
                            },
                            'file': {
                                     'level': 'DEBUG',
                                     'class': 'logging.handlers.RotatingFileHandler',
                                     'formatter': 'default',
                                     'filename' : 'run.log',
                                     'maxBytes':    20 * 1024 * 1024,  # 10M
                                     'backupCount': 5,
                                     'encoding' : 'utf8',
                            }
                },
               'loggers' : {
                            # 定义了一个logger
                            '' : {
                                          'level' : 'DEBUG',
                                          'handlers' : ['console', 'file'],
                                          'propagate' : True
                            }
                }
    }
    logging.config.dictConfig(LOGGING)