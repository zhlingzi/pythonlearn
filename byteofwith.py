# -*- coding:utf8 -*-
''' Create on "2017/10/5 8:40"
    _author_="zhao ling"
    Poject: 《byte of python》
    with 来打开文件，可以保证最后文件会被关闭
 '''

with open('try.txt') as f:
    for line in f:
        print(line)
