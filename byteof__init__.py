# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/4 12:28"

# 《byte of python》
# python类中，有很多方法的名称具有特殊含义 ,如__xxx__,__xxx,_xxx
# __init__ 方法在类对象实例化时被立即运行，可以进行初始化操作
# 此方法不需要显示调用
# 这里name是一个局部变量，只存在于函数体内，将其绑定到self上
# 其他的函数体就可以通过self.name访问

class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is ',self.name)

P = Person('Zhao Ling')
P.say_hi()