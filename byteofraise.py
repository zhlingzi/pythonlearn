# -*- coding:utf8 -*-
''' Create on "2017/10/5 8:11"
    _author_="zhao ling"
    Poject: 《byte of python》

    用raise 来引发一次异常，需要提供错误名、异常名和要抛出异常的对象
    此处的错误和异常是直接或间接从属于 Exception 的派生类
    此处自定义错误类，使用 try except 验证
 '''

class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self,lenght,atleast):
        self.lenght = lenght
        self.atleast = atleast


try:
    text = input('Enter-->')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
    # 其他工作可以继续
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long ,excepted at least {1}').format(ex.lenght,ex.atleast))
else:
    print('No exception was raised.')

