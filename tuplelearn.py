# -*- coding:utf8 -*-
# _author_="zhao ling"
# _date_="2017/10/2 18:17"

# 元组
# 创建
tuple1 = ()
print('tuple1 : ',tuple1)
tuple2 = ('one',)
print('tuple2 : ',tuple2)
tuple3 = (1,2,3,['a','b','c'])
print('tuple3 : ',tuple3)
# 拼接
tuple4 = tuple1 + tuple2 + tuple3
print('tuple4 : ',tuple4)
# 计数
print('count : ',tuple2.count('one'))
# 索引
print('index : ',tuple3.index(1))
# 遍历
print('tuple4 : ',len(tuple4))
print('Element : ')
for i in tuple4:
    print(i, end= ' ')
print()
# 更改列表
tuple3[3][0] = '更改'
print('tuple3 : ',tuple3)
