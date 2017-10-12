# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/4 12:09"

# 这是《byte of python》一书中的面向对象编程篇（oop）
# class可以创造一种新的类型，object是类的实例
# 类的属性：字段和方法
# 字段：实例变量和类变量
# 类方法与普通函数的区别：
# 类方法必须在参数列表开头提供一个额外的名字，调用时不需要赋值，
# python会为它提供对象本身
# 按照惯例，这个参数写为self
# 这个过程是： 有一个类 Myclass，这个类有一个对象 myobject，
# 调用了类方法method并提供了两个参数args1，args2
# myobject.method(args1，args2) 等同于
# Myclass.method(myobject，args1，args2)

# 最简类
class Person:
    pass

p = Person()
print(p,Person)
