# -*- coding:utf8 -*-
''' Create on "2017/10/5 9:05"
    _author_="zhao ling"
    Poject: 《byte of python》
    如何返回多个值，可以使用元组
    最快的交换方法是 a,b = b,a
    会将表达式右边解释成具有两个值的元组，再分别赋值到左边
 '''

def get():
    return (2,3)

x,y = get()

print(x,y)

def get2():
    return [1,2,3]

a,b,c = get2()
print(a,b,c)