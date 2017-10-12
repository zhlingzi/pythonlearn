# -*- coding:utf8 -*-
''' Create on "2017/10/5 16:14"
    _author_="zhao ling"
    Poject: 《byte of python》
    在函数中接收元组和字典 *元组 **字典
    * 和 ** 会分别以元组和字典形式往函数传参
    但在函数初始化时，只需要给多的参数即可，不一定要写成元组()、字典{}形式
 '''
def powersum(power,*args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i,power)
    return total

p = powersum(2,2,3,4)
print(p)
#print(powersum(2,'a'))
