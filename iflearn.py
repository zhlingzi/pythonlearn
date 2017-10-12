# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:19"

n = int(input('Enter integer n : '))
if n > 20:
    print('%d > 20'%n)
elif n > 10:
    print('20 > %d > 10'%n)
else:
    print('%d <= 10'%n)