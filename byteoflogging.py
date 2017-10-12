# -*- coding:utf8 -*-
''' Create on "2017/10/5 8:48"
    _author_="zhao ling"
    Poject: 《byte of python》
    标准库 日志 logging
 '''

import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'text.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),'text.log')

print('Logging to ', logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w'
)

logging.debug('Start of the progrem')
logging.info('Doing something')
logging.warning('Dying now')


