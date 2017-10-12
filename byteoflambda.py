# -*- coding:utf8 -*-
''' Create on "2017/10/5 9:17"
    _author_="zhao ling"
    Poject: 《byte of python》
    lambda 需要参数，后跟表达式，表达式的值是返回值

 '''

li = [{'x':1,'y':4},{'x':2,'y':3}]
li.sort(key=lambda i : i['y'])
print(li)