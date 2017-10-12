# -*- coding:utf8 -*-
''' Create on "2017/10/5 8:24"
    _author_="zhao ling"
    Poject: 《byte of python》
    try
    finally 无论是否发生异常，需要的操作可以放在其中
    如，打开一个文件，无论是否有异常，都希望最后能关闭它
 '''

import sys
import time

f = None
try:
    f = open('try.txt')
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
        sys.stdout.flush()  # 这句是什么意思？
#        print('Please ctrl+d now')  ???
#        print('Please ctrl+c now')  ???
        # 确保运行
        time.sleep(2)
except IOError:
    print('Could not find file try.txt')
except EOFError:
    print('Why did you do an EOF on me')
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file')
finally:
    if f:
        f.close()
    print('(Cleaning up: Closed the file)')