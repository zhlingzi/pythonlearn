# -*- coding:utf8 -*-
''' Create on "2017/10/5 16:43"
    _author_="zhao ling"
    Poject: 《byte of python》
    装饰器是应用包装函数的快捷方式
 '''
from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log = logging.getLogger('retry')

def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPS = 5
        for attemp in range(1,MAX_ATTEMPS+1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception('Attempt %s/%s failed : %s',
                              attemp,
                              MAX_ATTEMPS,
                              (args,kwargs))
                sleep(10 * attemp)
        log.critical('All %s attemps failed : %s',
                     MAX_ATTEMPS,
                     (args,kwargs))
    return wrapped_f

counter = 0

@retry
def save_to_database(arg):
    print('Write to a database or make a network call or etc.')
    print('This will be automatically retried if exception is thrown.')
    global counter
    counter += 1
    # 这将是第一次调用时抛出异常
    # 在第二次运行时将正常工作，重试
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    save_to_database('Some bad value')