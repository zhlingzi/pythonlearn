# -*- coding:utf8 -*-
''' Create on "2017/10/4 19:24"
    _author_="zhao ling"
    Poject: 《byte of python》
 '''
# string 输出
'''
s1 = 'zhao'
s2 = 'ling'
print('{0} {1}'.format(s1,s2))
print('{} {}'.format(s1,s2))
print('{1} {0}'.format(s1,s2))
'''

print('{}'.format(1.0/3))
print('{:.3f}'.format(1.0/3))
print('{1:.3f}'.format(1.0/3,2.0/3))
# 对数字似乎无用
print('{:_^11}'.format(1.0/3))
print('{:_^11}'.format('1.0/3'))
# 观察区别
print('{:_^}'.format('hello'))
print('{:_^11}'.format('hello'))

# re正则模块，所有值都加上r
print(r'This is a raw string.\n\t\r')
print(R'This is a raw string.\n\t\r')
