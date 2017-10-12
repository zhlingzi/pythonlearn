# -*- coding:utf8 -*-
''' Create on "2017/10/5 16:36"
    _author_="zhao ling"
    Poject: 《byte of python》
    assert 用以断言某事是真的
    可单独使用，和继承自 Exception类的不同
    断言不为真时，会出现 assertionError
 '''

# 判断列表不为空
mylist = ['item']
assert len(mylist) >= 1

mylist.pop()
assert len(mylist) >= 1